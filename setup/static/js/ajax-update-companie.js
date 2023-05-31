$("button#btnUpdateCompanie").on("click", function (e) {
    e.preventDefault();

    name = $("input#exampleInputNameCompanieUpdate").val();
    active = $("select#selectActiveCompanieUpdate").val();
    companie_id = $("form.form-update-companie").attr("data-title");

    $.ajax({
        type: 'GET',
        url: 'update-companie/' + companie_id,
        data: {
            'name': name,
            'active': active,
        },
        datatype: "json",
        success: function (data) {
            window.location = "/details/" + companie_id;
        }
    });
});
