$(document).ready(function(){  
  $("#image").append("<div class='col-4 mx-auto'></div><div class='col-4 mx-auto'><img src=" + img_link + " width = '300', height = '250'></div><div class='col-4 mx-auto'></div>")

  $.each(options, function(index, value){
     let btn = $("<div class='col-md-1'><button onclick='myFunction(`"+ value +"`,`"+quiz_id+"`)'>"+value+"</button></div>");
     $("#options").append(btn)
  });
})

function myFunction(user_answer, quiz_id) {
  let answer_info = {"user_answer": user_answer, "quiz_id": quiz_id}
  console.log(answer_info)
  $.ajax({
      type: "POST",
      url: "checkanswer",                
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(answer_info),
      success: function(result){
        let notice= result["notice"]
        console.log(notice)
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });

  if(end_flag == 0){
        $("#next-button").html("<a href='/quiz/"+ next_id+ "'><button><span>  Next  </span></button></a>")
  }
  else{
        $("#next-button").html("<a href='/quizend'><button><span>  Look at result  </span></button></a>")
   }
}
