---
name: revisao-entrega
description: Verifica a integridade do projeto Django antes de enviar ao GitIngest, GitHub ou avaliador.
---
# Revisão de entrega

## Quando usar
Antes de qualquer commit final, geração de resumo ou deploy.

## Procedimento
1. Identifique a raiz pelo arquivo `manage.py` e confirme o ambiente virtual.
2. Execute `python manage.py check` e corrija os erros exibidos.
3. Execute `python manage.py makemigrations --check --dry-run` para detectar modelos sem migração.
4. Execute `python manage.py test` e registre falhas e limitações.
5. Confirme as URLs de login, recuperação de senha, listagens e `/assistente/`.
6. Inspecione templates de listagem, `website/modelo.html`, tag `paginacao.py`, `complementos.js` e `mascaras.js`.
7. Confirme `requirements.txt`, `app.yaml`, `AGENTS.md`, `contexto_projeto.md` e todas as skills.
8. Verifique se nenhum `.env`, segredo, senha ou banco SQLite está no Git; nunca imprima credenciais em logs.
9. Gere o GitIngest incluindo `*.html`, `*.py`, `*.md`, `*.js`, `*.yaml`, `*.txt`, com exclusões de migrações e ambientes.
10. Execute `git log --oneline` e inclua a saída real na entrega.
11. Só declare deploy concluído após validar a URL real da aplicação e o funcionamento do serviço.

## Critério de conclusão
Checklist documentado com evidências; nenhuma verificação pendente deve ser declarada como aprovada.
