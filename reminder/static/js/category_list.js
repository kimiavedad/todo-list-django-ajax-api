$(document).ready(function(){
    console.log('fsssdj')
    $(".button").click(function(event){
        event.preventDefault();
        console.log($(this).text());
        $.ajax({
            type: 'POST',
            url: $(this).attr('href'),
            data: {'csrfmiddlewaretoken': CSRF_TOKEN},
            success: function(response) {
                show_categories(response)
            }
        });
    
    })

    function show_categories(data){
        $(".list-group").empty()
        console.log(data)
        if (data['object_list']){
            for (const [key, value] of Object.entries(data['object_list'])) {
                $(".list-group").append('<a class="list-group-item list-group-item-action"></a>');
                $(".list-group a:last-child").text(value['name']);
                $(".list-group a:last-child").attr('href', value['pk']);
            }
        }
        else{
            $(".list-group").append()
        }

    }
})