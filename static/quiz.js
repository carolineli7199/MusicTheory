const { Renderer, Stave, Voice, StaveNote, Formatter } = Vex.Flow;

$(document).ready(function(){
  $("#image").append("<div class='col-4 mx-auto'></div>")

  let staffdiv = document.createElement("div")
  staffdiv.className = "col-4 mx-auto"
  console.log(staffdiv)
  let renderer = new Renderer(staffdiv, Renderer.Backends.SVG);
  renderer.resize(400, 200)
  let context = renderer.getContext()

  let stave = new Stave(10, 40, 350);

  // add the clef if required (the staff learning page does not need it)
  if (staff_data["clef"] === 1) {
    stave.addClef("treble")
  }
  if (staff_data["clef"] === 2) {
    stave.addClef("bass")
  }

  // add notes if necessary
  if (staff_data["notes"].length > 0) {
    let notes = []
    for (let note of staff_data["notes"]) {
      notes.push(new StaveNote({keys: note["keys"], duration: "q"}))
    }
    let voice = new Voice({num_beats: staff_data["notes"].length, beat_value: 4})
    voice.addTickables(notes)
    new Formatter().joinVoices([voice]).format([voice], 350)
    voice.draw(context, stave)
  }

  stave.setContext(context).draw()

  document.getElementById("image").append(staffdiv)
  $("#image").append("<div class='col-4 mx-auto'></div>")

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
