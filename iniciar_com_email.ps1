# Execute dentro da pasta do projeto: .\iniciar_com_email.ps1
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
Write-Host 'CONFIGURACAO DE ENVIO DE EMAIL - HOTEL MARAVILHA' -ForegroundColor Cyan
Write-Host 'Use as credenciais SMTP do Brevo (nao a senha do Gmail).'
$servidor = Read-Host 'Servidor SMTP [smtp-relay.brevo.com]'
if ([string]::IsNullOrWhiteSpace($servidor)) { $servidor = 'smtp-relay.brevo.com' }
$login = Read-Host 'Login SMTP do Brevo'
$senhaSegura = Read-Host 'Chave SMTP do Brevo (nao aparece na tela)' -AsSecureString
$remetente = Read-Host 'Email remetente verificado no Brevo'
$ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($senhaSegura)
try { $senha = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr) }
finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr) }
$env:DJANGO_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
$env:EMAIL_HOST = $servidor
$env:EMAIL_PORT = '587'
$env:EMAIL_USE_TLS = 'true'
$env:EMAIL_HOST_USER = $login
$env:EMAIL_HOST_PASSWORD = $senha
$env:DEFAULT_FROM_EMAIL = $remetente
Remove-Variable senha -ErrorAction SilentlyContinue
Write-Host 'Iniciando Django. Para parar, pressione Ctrl+C.' -ForegroundColor Green
python manage.py runserver
Write-Host 'Servidor encerrado. Se houve erro, leia a mensagem acima.'
Read-Host 'Pressione Enter para fechar'
