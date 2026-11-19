$ErrorActionPreference = 'Stop'
python -m pip install -r requirements.txt
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
Write-Host 'Verificacoes concluidas. Confira tambem os templates no GitIngest e o deploy real.'
