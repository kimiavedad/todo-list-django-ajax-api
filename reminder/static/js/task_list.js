$(document).ready(function(){

    $(".button").click(function(event){
        event.preventDefault();
        console.log($(this).text());
        $.ajax({
            type: 'POST',
            url: $(this).attr('href'),
            data: {'csrfmiddlewaretoken': CSRF_TOKEN},
            success: function(response) {
                show_tasks(response)
            }
        });
    })

    function show_tasks(data){
        $("#tasks_list").empty()
        if (data['object_list']){
            for (const [key, value] of Object.entries(data['object_list'])) {

                var index = document.createElement('th');
                var shcedule = document.createElement('th');
                var title = document.createElement('th');
                var detail = document.createElement('th');
              
                index_text = document.createTextNode(parseInt(key) + 1);
                index.append(index_text)
                shcedule_text = document.createTextNode(value['schedule']);
                shcedule.append(shcedule_text)
                title_text = document.createTextNode(value['title']);
                title.append(title_text)
                detail.innerHTML ="<a class='btn btn-info'>Detail</a>";

                a = detail.getElementsByTagName('a')[0]
                a.href = value['pk']

                $("#tasks_list").append('<tr></tr>');
                $("#tasks_list tr:last-child").append(index);
                $("#tasks_list tr:last-child").append(shcedule);
                $("#tasks_list tr:last-child").append(title);
                $("#tasks_list tr:last-child").append(detail);
              }
        }
        else{
            $("#tasks_list").append()
        }

    }
})