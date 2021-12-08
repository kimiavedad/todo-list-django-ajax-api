$(document).ready(function(){

    $("#task-form").submit(function(event){
        // event.preventDefault()
        const data = new FormData(event.target);
        const formJSON = Object.fromEntries(data.entries()); 
        console.log(formJSON)
        formJSON.categories = data.getAll('categories');
        formJSON['csrfmiddlewaretoken'] = CSRF_TOKEN;
        send_ajax(formJSON)
    })

    function send_ajax(data){
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