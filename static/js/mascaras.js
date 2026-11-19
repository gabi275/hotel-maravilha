$(function () {
    function mascaraTelefone(valor) {
        return valor.replace(/\D/g, '').length > 10
            ? '(00) 00000-0000'
            : '(00) 0000-00009';
    }

    function opcoesTelefone() {
        return {
            onKeyPress: function (valor, evento, campo, opcoes) {
                campo.mask(mascaraTelefone(valor), opcoes);
            }
        };
    }

    $('input[name]').each(function () {
        var campo = $(this);
        var identificador = (campo.attr('name') + ' ' + (campo.attr('id') || '')).toLowerCase();

        if (identificador.indexOf('cpf') !== -1) {
            campo.mask('000.000.000-00');
        } else if (identificador.indexOf('cnpj') !== -1) {
            campo.mask('00.000.000/0000-00');
        } else if (identificador.indexOf('cep') !== -1) {
            campo.mask('00000-000');
        } else if (
            identificador.indexOf('telefone') !== -1 ||
            identificador.indexOf('celular') !== -1 ||
            identificador.indexOf('whatsapp') !== -1
        ) {
            campo.mask(mascaraTelefone, opcoesTelefone());
        }
    });
});
