$("button#btnCreateCNPJ").on("click", function (e) {
    e.preventDefault();

    name = $("input#exampleInputName").val();
    cnpj = $("input#exampleInputCnpj").val()
    active = $("select#select_active_cnpj").val();
    companie_id = $("form.form-create-cnpj").attr("data-title")

    $.ajax({
        type: 'GET',
        url: 'addnew-cnpj/' + companie_id,
        data: {
            'name': name,
            'cnpj': cnpj,
            'active': active,
        },
        datatype: "json",
        success: function (data) {
            $('#exampleInputName').val('');
            $('#exampleInputCnpj').val('');
            $('#modalCreateCNPJ').modal('hide');
            console.log(data)
            window.location = "/details/" + companie_id;
        }
    });
});
