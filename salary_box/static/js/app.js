$("#friend-form").submit(function (e) {
    e.preventDefault();
    var serializedData = $(this).serialize();
    $.ajax({
        type: 'POST',
        url: "add-company/",
        data: serializedData,
        success: function (response) {
            
        },
        error: function (response) {
            console.log('error')
        }
    })
})