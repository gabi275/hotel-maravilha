---
name: seguranca-django
description: Audita autenticação, autorização, isolamento de registros e segredos no Hotel Maravilha.
---
# Segurança Django

## Quando usar
Ao alterar models, views, permissões, recuperação de conta ou configuração de produção.

## Procedimento
1. Liste as views Create, Update, Delete, List e Detail e seus mixins.
2. Confirme `LoginRequiredMixin` em páginas privadas.
3. Para operações de escrita, verifique autorização no servidor em GET e POST, não apenas ocultação de botões.
4. Faça login como `convidado` e como membro do grupo `Convidado`; confirme HTTP 403 para cadastro, edição e exclusão.
5. Teste que registros de outro usuário não podem ser lidos, editados ou excluídos pela troca do `pk` na URL.
6. Confira que FKs selecionáveis nos formulários respeitam a autorização do usuário.
7. Valide CSRF nos formulários e proteção contra redirecionamento aberto.
8. Revise `settings.py`: segredos devem vir de variáveis de ambiente, `DEBUG=False` em produção e hosts autorizados definidos.
9. Verifique que e-mails de recuperação não revelam senhas e não enumeram usuários.
10. Execute testes automatizados e registre evidências e riscos restantes.

## Restrições
Nunca exponha `DATABASE_URL`, `SECRET_KEY`, tokens SMTP ou senhas. Nunca declare seguro sem testes.
