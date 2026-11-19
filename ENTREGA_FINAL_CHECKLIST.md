# Hotel Maravilha — entrega e verificações

## Implementado no código
- CRUD com controle de propriedade; restrições de convidado no servidor e ocultação de ações nos templates.
- Mensagens Django em `website/templates/website/modelo.html`.
- Django Filter em `ReservaList`, filtros e paginação com tag personalizada na listagem.
- jQuery Mask, DataTables e Bootbox carregados pelo template base.
- Recuperação de senha e usuário por e-mail configurável por ambiente.
- `AGENTS.md`, três skills e `contexto_projeto.md`.
- App `ia` com tela `/assistente/`, respostas locais e integração **opcional** com API de modelo generativo via `OPENAI_API_KEY`. Sem chave, funciona em modo local, sem alegar usar IA generativa.
- `app.yaml` e `requirements.txt` para implantação.

## Execução local (PowerShell)
```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
python manage.py runserver
```
Não sobrescreva `db.sqlite3` existente: o ZIP não o contém. Use a pasta de projeto atual e mantenha cópia do banco antes de qualquer migração.

## Ativar IA generativa (opcional, custo por uso)
Defina `OPENAI_API_KEY` **apenas** no ambiente de execução, não no GitHub nem em arquivos rastreados. Opcionalmente, `OPENAI_MODEL=gpt-4.1-mini`. A integração usa HTTPS com timeout e fallback para respostas locais. É necessário ter uma chave válida e acesso à API.

## Evidências da avaliação
No GitIngest, para capturar todos os templates, use o Include `*.py, *.md, *.js, *.yaml, *.txt, *.html, */.agents/skills/*` e as exclusões recomendadas pelo professor. O filtro fornecido pelo professor não inclui `modelo.html` nem todas as listagens; confira manualmente a árvore de arquivos. Não copie segredos.

Execute `git --no-pager log --oneline` **no repositório real** e cole a saída. Um ZIP não preserva o histórico Git. Para publicação, configure credenciais do projeto GCP, variáveis de ambiente, banco PostgreSQL e e-mail, rode `gcloud app deploy` somente com autorização e confirme a URL em produção. Não há comprovação de deploy neste pacote.

## Verificações pendentes
Não foi possível instalar dependências nem executar testes Django neste ambiente (sem acesso à rede). É indispensável rodar os comandos acima no VS Code e resolver qualquer erro antes da avaliação. A integração externa da IA requer credencial e rede para teste real. Não declare deploy ou testes concluídos sem evidências.
