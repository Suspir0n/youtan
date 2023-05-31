$("a#updateCNPJ").on("click", function (e) {
    e.preventDefault();

    cnpj_id = $("a.update-cnpj").attr("data-title")

    $.ajax({
        type: 'GET',
        url: 'list-data-for-update-cnpj/' + cnpj_id,
        data: {},
        datatype: "json",
        success: function (data) {
            $('#exampleInputCompanieUpdate').val(data.context.companie);
            $('#exampleInputCNPJUpdate').val(data.context.cnpj);
            $('#SelectActiveEditCNPJOption').val(data.context.active);
            $('#ModalEditCNPJ').modal('show');
        }
    });
});

$("button#btnUpdateCNPJ").on("click", function (e) {
    e.preventDefault();

    companie = $("input#exampleInputCompanieUpdate").val();
    cnpj = $("input#exampleInputCNPJUpdate").val();
    active = $("select#SelectActiveEditCNPJ").val();
    cnpj_id = $("a.update-cnpj").attr("data-title");
    companie_id = $("form.form-update-cnpj").attr("data-title");


    $.ajax({
        type: 'GET',
        url: 'update-cnpj/' + cnpj_id,
        data: {
            'companie': companie,
            'cnpj': cnpj,
            'active': active,
        },
        datatype: "json",
        success: function (data) {
            $('#exampleInputCompanie').val('');
            $('#exampleInputCnpj').val('');
            $('#ModalEditCNPJ').modal('hide');
            window.location = "/details/" + companie_id;
        }
    });
});

