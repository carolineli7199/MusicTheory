const { Renderer, Stave, Voice, StaveNote, Formatter } = Vex.Flow;

$(document).ready(function () {
  $("#learning-container").prepend(
    "<div id='question' class='row justify-content-md-center'></div>"
  );
  $("#question").append("<div class='col-md-auto' id='q_block'></div>");
  $("#q_block").append(
    "<div class='col mx-auto'><div class='ques'> <b> Question " +
      quiz_id +
      ":</b> " +
      question +
      "</div></div>"
  );
  if (type == "mc") {
    // $("#image").append("<div class='col-4 mx-auto'></div>");

    let staffdiv = document.createElement("div");
    staffdiv.className = "col-4 mx-auto";
    console.log(staffdiv);
    let renderer = new Renderer(staffdiv, Renderer.Backends.SVG);
    renderer.resize(370, 200);
    let context = renderer.getContext();

    let stave = new Stave(10, 40, 350);

    // add the clef if required (the staff learning page does not need it)
    if (staff_data["clef"] === 1) {
      stave.addClef("treble");
    }
    if (staff_data["clef"] === 2) {
      stave.addClef("bass");
    }

    // add notes if necessary
    if (staff_data["notes"].length > 0) {
      let notes = [];
      for (let note of staff_data["notes"]) {
        notes.push(new StaveNote({ keys: note["keys"], duration: "q" }));
      }
      let voice = new Voice({
        num_beats: staff_data["notes"].length,
        beat_value: 4,
      });
      voice.addTickables(notes);
      new Formatter().joinVoices([voice]).format([voice], 350);
      voice.draw(context, stave);
    }

    stave.setContext(context).draw();

    document.getElementById("image").append(staffdiv);
    // $("#image").append("<div class='col-4 mx-auto'></div>");
    setMC();
  } else if (type == "clicknode") {
    build_block();
  }
});

function setMC() {
  console.log(options.length);
  if (options.length == 2) {
    let space = $("<div class='col-md-3'></div>");
    $("#options_c").append(space);
  }
  $.each(options, function (index, value) {
    let cont = $("<div class='col-md-10'>" + contents[index] + "</div>");
    let btn = $(
      "<div class='col-md-2'><button class='mc-button' onclick='getNext(`" +
        value +
        "`,`" +
        quiz_id +
        "`)'>" +
        value +
        "</button></div>"
    );
    if (has_contents == 0) {
      $("#options_c").append(btn);
    }
    if (has_contents == 1) {
      $("#options").append(
        "<div class='row' id='options_block" + index + "'> </div>"
      );
      $("#options_block" + index)
        .append(btn)
        .append(cont);
    }
  });
}

function build_block() {
  let str =
    '<div class="col-4 mx-auto"> <svg width="800" height="400" viewBox="0 0 400 200" style="width: 400px; height: 200px;"><g class="vf-stave" id="vf-auto1000">' +
    '<path id="b1" onclick=checkNum_num(1) stroke-width="5" stroke-dasharray="none" fill="none" stroke="#999999" d="M10 80L360 80"></path> <rect id="b2" onclick=checkNum_num(2) x="10" y="83" width="350" height="10" style="fill:rgb(255,255,255);"/>' +
    '<path id="b3" onclick=checkNum_num(3) stroke-width="5" stroke-dasharray="none" fill="none" stroke="#999999" d="M10 95L360 95"></path> <rect id="b4" onclick=checkNum_num(4) x="10" y="98" width="350" height="10" style="fill:rgb(255,255,255);"/>' +
    '<path id="b5" onclick=checkNum_num(5) stroke-width="5" stroke-dasharray="none" fill="none" stroke="#999999" d="M10 110L360 110"></path><rect id="b6" onclick=checkNum_num(6) x="10" y="113" width="350" height="10" style="fill:rgb(255,255,255);"/>' +
    '<path id="b7" onclick=checkNum_num(7) stroke-width="5" stroke-dasharray="none" fill="none" stroke="#999999" d="M10 125L360 125"></path><rect id="b8" onclick=checkNum_num(8) x="10" y="128" width="350" height="10" style="fill:rgb(255,255,255);"/>' +
    '<path id="b9" onclick=checkNum_num(9) stroke-width="5" stroke-dasharray="none" fill="none" stroke="#999999" d="M10 140L360 140"></path> ';
  str +=
    '<rect x="10" y="79" width="1" height="60" fill="black"></rect><rect x="360" y="79" width="1" height="60" fill="black"></rect><g class="vf-clef" id="vf-auto1003">' +
    "</g></g></svg></div>";
  $("#clickstaff").append(str);
}

function checkNum_num(id) {
  console.log(id);
  let list = [];
  if (staff_data["clef"] === 1) {
    list = ["F", "E", "D", "C", "B", "A", "G", "F", "E"];
  }
  if (staff_data["clef"] === 2) {
    list = ["A", "G", "F", "E", "D", "C", "B", "A", "G"];
  }
  console.log(list[id - 1]);

  for (let i = 1; i < 10; i++) {
    if (i % 2 == 0) {
      $("#b" + i).css("fill", "rgb(255,255,255)");
      $("#b" + i).css("stroke", "rgb(255,255,255)");
    } else {
      $("#b" + i).css("stroke", "#999999");
      $("#b" + i).css("fill", "rgb(255,255,255)");
    }
    //$("#b" + i).css("fill", "rgb(255,255,255)");
  }
  $("#b" + id).css("stroke", "#27537a");
  $("#b" + id).css("fill", "#27537a");

  getNext(list[id - 1], quiz_id + "");
}

function checkAnswer(user_answer, quiz_id) {
  let answer_info = { user_answer: user_answer, quiz_id: quiz_id };
  $.ajax({
    type: "POST",
    url: "checkanswer",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(answer_info),
    success: function (result) {
      let notice = result["notice"];
      console.log(notice);
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
}

function getNext(user_answer, quiz_id) {
  if (end_flag == 0) {
    $("#next-button").html(
      "<a href='/quiz/" +
        next_id +
        "'><button class='next-button-start' onclick='checkAnswer(`" +
        user_answer +
        "`,`" +
        quiz_id +
        "`)'>" +
        "<span class='next-button-wrapper'>  Next  </span></button></a>"
    );
  } else {
    $("#next-button").html(
      "<a href='/quizend'><button class='next-button-start' onclick='checkAnswer(`" +
        user_answer +
        "`,`" +
        quiz_id +
        "`)'>" +
        "<span lass='next-button-wrapper'>>  Look at result  </span></button></a>"
    );
  }
}
