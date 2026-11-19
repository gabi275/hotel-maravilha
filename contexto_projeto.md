# Contexto do projeto — Hotel Maravilha

## Objetivo
Sistema Django de gestão hoteleira para cadastro e consulta de hóspedes, reservas, quartos, tipos de quarto, status de reserva e hospedagens.

## Arquitetura
- Projeto Django: `pw2026`; aplicação de gestão: `website`; assistente local: `ia`.
- Banco SQLite no desenvolvimento ou PostgreSQL com `DATABASE_URL` por variável de ambiente.
- Autenticação nativa do Django; recuperação de senha e usuário por e-mail.
- Templates Bootstrap, scripts jQuery Mask, DataTables e Bootbox; Django Filter para reservas.
- App `ia`: orientações baseadas em regras locais sobre o uso do sistema. Não é integração com LLM nem possui API externa.

## Permissões
- Cadastros gerais de quartos e status exigem equipe/gerência.
- Registros de hóspedes, reservas e hospedagens pertencem ao usuário que os criou.
- Usuário `convidado` ou membro do grupo `Convidado` não pode cadastrar, editar ou excluir.
- Autorização deve ser aplicada no servidor, não somente em templates.

## Comandos de validação
`python manage.py check`
`python manage.py makemigrations --check --dry-run`
`python manage.py test`
`python manage.py runserver`

## Entrega
Incluir todos os templates (`*.html`) no GitIngest. A publicação no Google App Engine não foi comprovada por este pacote; `app.yaml` por si só não comprova deploy.
