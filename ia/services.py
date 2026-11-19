"""Assistente local baseado em regras, sem API externa nem acesso irrestrito ao banco.

Responde orientações sobre o sistema. Não se apresenta como IA generativa.
"""
import unicodedata


def normalizar(texto):
    return ''.join(c for c in unicodedata.normalize('NFKD', texto.lower()) if not unicodedata.combining(c))


def responder(pergunta, usuario):
    q = normalizar(pergunta)
    convidado = usuario.username.lower() == 'convidado' or usuario.groups.filter(name='Convidado').exists()
    if any(x in q for x in ('senha', 'login', 'entrar', 'acesso')):
        return 'Para alterar a senha, use a opção Alterar Senha no menu de usuário. Se não conseguir entrar, use Recuperar senha na página de login.'
    if any(x in q for x in ('hospede', 'hospedes')):
        return 'Acesse Listagens > Hóspedes para consultar seus registros. ' + ('O perfil convidado não pode cadastrar, editar ou excluir.' if convidado else 'Para registrar um novo hóspede, use Cadastros > Hóspede.')
    if any(x in q for x in ('reserva', 'reservar')):
        return 'Acesse Listagens > Reservas para consultar suas reservas. ' + ('Seu perfil é somente leitura.' if convidado else 'Para criar uma reserva, acesse Cadastros > Reserva e informe os dados solicitados.')
    if any(x in q for x in ('quarto', 'acomodacao')):
        return 'Consulte Listagens > Quartos e Tipos de Quarto. O gerenciamento de quartos exige permissão de gerente.'
    if any(x in q for x in ('hospedagem', 'check-in', 'check out', 'checkout')):
        return 'Use Listagens > Hospedagens para acompanhar os registros. A criação e alteração exigem autorização.' if convidado else 'Acesse Listagens > Hospedagens para consultar e Cadastros > Hospedagem para registrar uma hospedagem.'
    if any(x in q for x in ('convidado', 'permissao', 'permissoes', 'cadastrar', 'editar', 'excluir')):
        return 'O convidado pode consultar as páginas permitidas, mas não pode cadastrar, editar nem excluir. Para realizar alterações, entre com uma conta autorizada.'
    if any(x in q for x in ('ajuda', 'funciona', 'menu', 'sistema')):
        return 'Posso orientar sobre hóspedes, reservas, quartos, hospedagens, permissões e recuperação de senha. Escolha um desses assuntos.'
    return 'Não encontrei uma orientação específica. Pergunte sobre reservas, hóspedes, quartos, hospedagens, permissões ou recuperação de senha.'


# Integração com Gemini via API REST, sem dependências extras.
# A chave é lida exclusivamente da variável de ambiente GEMINI_API_KEY.
def responder_com_ia(pergunta, usuario):
    import os
    import json
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    from urllib.parse import quote

    chave = os.environ.get('GEMINI_API_KEY', '').strip()
    if not chave:
        return responder(pergunta, usuario), False

    convidado = usuario.username.lower() == 'convidado' or usuario.groups.filter(name='Convidado').exists()
    regras = (
        'Você é o assistente do sistema Hotel Maravilha. Responda em português brasileiro, '
        'com objetividade. Oriente sobre hóspedes, reservas, hospedagens, quartos e recuperação '
        'de senha. Não invente registros, disponibilidade, preços ou operações realizadas. '
        'Você não tem acesso ao banco de dados e não pode realizar cadastros. '
        'Não solicite senhas, chaves, dados de cartão ou documentos pessoais. '
        + ('Esta conta é convidada: somente leitura, sem cadastrar, editar ou excluir.' if convidado
           else 'Cadastros e alterações exigem permissões apropriadas.')
    )
    modelo = os.environ.get('GEMINI_MODEL', 'gemini-2.5-flash')
    endpoint = ('https://generativelanguage.googleapis.com/v1beta/models/'
                + quote(modelo, safe='') + ':generateContent')
    payload = json.dumps({
        'systemInstruction': {'parts': [{'text': regras}]},
        'contents': [{'role': 'user', 'parts': [{'text': pergunta}]}],
        'generationConfig': {'maxOutputTokens': 700, 'temperature': 0.3},
    }, ensure_ascii=False).encode('utf-8')
    req = Request(endpoint, data=payload, headers={
        'Content-Type': 'application/json', 'x-goog-api-key': chave,
    }, method='POST')
    try:
        with urlopen(req, timeout=15) as response:
            dados = json.load(response)
        textos = [parte.get('text', '') for item in dados.get('candidates', [])
                  for parte in item.get('content', {}).get('parts', [])]
        texto = '\n'.join(t for t in textos if t).strip()
        if texto:
            return texto, True
    except (URLError, HTTPError, TimeoutError, ValueError, OSError, KeyError, TypeError):
        pass
    return responder(pergunta, usuario), False
