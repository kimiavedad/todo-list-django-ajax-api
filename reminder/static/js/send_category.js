$(document).ready(function(){
    console.log("hi")
    $("#category-form").submit(function(event){
        event.preventDefault()
        const data = new FormData(event.target);
        const formJSON = Object.fromEntries(data.entries()); 
        formJSON['csrfmiddlewaretoken'] = CSRF_TOKEN;
        send_ajax(formJSON)
    })

    function send_ajax(data){
        console.log(data)
        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data: data,
        }).done(function(response){
            alert(response['message']);
            document.getElementById("category-form").reset();
        });
    }
})