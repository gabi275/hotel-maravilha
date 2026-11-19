# Hotel Maravilha — orientações para agentes
- Projeto Django 5.2, app `website`; preservar templates e URLs existentes.
- Nunca commitar `.env`, `db.sqlite3`, credenciais, dados pessoais ou arquivos coletados.
- `Hospede`, `Reserva` e `Hospedagem` pertencem ao usuário; proteger queryset e escolhas de FK.
- Cadastros gerais: escrita apenas staff ou grupo `Gerente`.
- Rodar `python manage.py check`, `python manage.py test` e `python manage.py makemigrations --check --dry-run` antes de entregar.
- Migrações devem preservar dados; não atribuir hóspedes antigos a um usuário arbitrário.
- Seguir as skills em `.agents/skills`.
