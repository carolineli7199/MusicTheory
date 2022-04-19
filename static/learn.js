$(document).ready(function(){  
    if (img_num == "1"){
        $("#image").append("<div class='col-4 mx-auto'></div><div class='col-4 mx-auto'><img src=" + img_links[0] + " width = '300', height = '250'></div><div class='col-4 mx-auto'></div>")
    }
    if (img_num == "2"){
        $("#image").append("<div class='col-3 mx-auto'><img src=" + img_links[0] + " width = '300', height = '250'></div><div class='col-3 mx-auto'><img src=" + img_links[1] + " width = '300', height = '250'></div>")
    }

    $.each(info, function(index, value){
        $("#info").append(value);
    });

    if(next_topic != null){
        $("#next-button").html("<a href='/learning/"+ next_id+ "'><button><span>  "+next_topic+"  </span></button></a>")
    }
    else{
        $("#next-button").html("<a href='/quiz/1'><button><span>  Test  </span></button></a>")
    }
})