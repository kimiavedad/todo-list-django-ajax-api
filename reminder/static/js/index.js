$(document).ready(function(){
    console.log("inside index.js")

    $("#task-form").submit(function(event){
        const data = new FormData(event.target);
        const formJSON = Object.fromEntries(data.entries());
        // formJSON.snacks = data.getAll('snacks');
        send_ajax(formJSON)
    })

    function send_ajax(data){
        data['csrfmiddlewaretoken'] = CSRF_TOKEN,
        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data: data,
            success: function(response) {
                alert("Your task added successfully!");
            }
        });
    }
})