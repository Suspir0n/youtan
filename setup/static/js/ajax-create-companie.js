$("button#btn-create-companie").on("click", function (e) {
    e.preventDefault();

    name = $("input#exampleInputCompanie").val();
    active = $("select#activeCompanie").val();

    $.ajax({
        type: 'GET',
        url: 'addnew-companie/',
        data: {'name': name, 'active': active, },
        datatype: "json",
        success: function (data) {
            $('#exampleInputCompanie').val('');
            $('#modalCreateCompanie').modal('hide');
            window.location = "/";
        }
    });
});
