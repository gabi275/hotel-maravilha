/* Complementos jQuery: DataTables e Bootbox (máscara em mascaras.js). */
$(function () {
    // DataTables em listas pequenas; listas com paginação Django usam paginação do servidor.
    $('table.table').each(function () {
        if (!$(this).closest('.card').find('nav .pagination').length && $.fn.DataTable) {
            $(this).DataTable({paging: false, searching: true, info: false, language: {search: 'Pesquisar:', zeroRecords: 'Nenhum registro encontrado'}});
        }
    });
    $('a[href*="/excluir/"]').on('click', function (event) {
        if (typeof bootbox === 'undefined') return;
        event.preventDefault();
        var link = this.href;
        bootbox.confirm({message: 'Deseja abrir a confirmação de exclusão?', buttons: {confirm: {label: 'Continuar'}, cancel: {label: 'Cancelar'}}, callback: function (ok) {if (ok) window.location.href = link;}});
    });
});
