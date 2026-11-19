# Hotel Maravilha — versão revisada

## O que foi acrescentado
- App `ia` com assistente local baseado em regras, acessível em `/assistente/` após login.
- Testes de acesso do assistente e de bloqueio de cadastro para convidado.
- Skills `revisao-entrega` e `seguranca-django` com frontmatter e procedimentos completos.
- `contexto_projeto.md` com arquitetura e permissões.
- Link para o assistente no menu principal.

## Instalação no Windows
1. Extraia o ZIP e abra a pasta `hotel-maravilha-main` no VS Code.
2. `python -m pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py test`
5. `python manage.py runserver`

## Importante sobre dados
O ZIP não inclui `db.sqlite3`, pois o banco local não estava no pacote de origem. Se você substituir a pasta do projeto, preserve seu banco antigo e as variáveis de ambiente.

## Avaliação
No GitIngest, use `*.py, *.md, *.js, *.yaml, *.txt, *.html` no Include, com as exclusões exigidas pelo professor. O filtro original omite `modelo.html` e diversos templates de listagem.

O assistente entregue é funcional, mas baseado em regras. Se a rubrica exigir integração com LLM/API, isso ainda precisará ser implementado. Deploy no App Engine e `git log` precisam ser feitos no ambiente real.
