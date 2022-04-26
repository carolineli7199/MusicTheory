const { Renderer, Stave, Voice, StaveNote, Formatter } = Vex.Flow;

$(document).ready(function(){
    if (img_num == "1"){
        $("#imgs").append("<div class='col-4 mx-auto'></div>")

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

        document.getElementById("imgs").append(staffdiv)
        $("#imgs").append("<div class='col-4 mx-auto'></div>")
    }
    if (img_num == "2"){
        console.log(staff_data)
        for (const d of staff_data) {
            console.log(d)
            let staffdiv = document.createElement("div")
            staffdiv.className = "col-3 mx-auto"
            let renderer = new Renderer(staffdiv, Renderer.Backends.SVG);
            renderer.resize(400, 200)
            let context = renderer.getContext()

            let stave = new Stave(10, 40, 350);

            // add the clef if required (the staff learning page does not need it)
            if (d["clef"] === 1) {
                stave.addClef("treble")
            }
            if (d["clef"] === 2) {
                stave.addClef("bass")
            }

            // add notes if necessary
            if (d["notes"].length > 0) {
                let notes = []
                for (let note of d["notes"]) {
                    notes.push(new StaveNote({keys: note["keys"], duration: "q"}))
                }
                let voice = new Voice({num_beats: d["notes"].length, beat_value: 4})
                voice.addTickables(notes)
                new Formatter().joinVoices([voice]).format([voice], 350)
                voice.draw(context, stave)
            }

            stave.setContext(context).draw()
            document.getElementById("imgs").append(staffdiv)
        }


    }

    $.each(info, function(index, value){
        msg = $("<div/>");
        padmsg = msg.addClass("paddingbottom");
        padmsg.html(value);
        $("#info").append(padmsg);
    });

    if(next_topic != null){
        $("#next-button").html("<a href='/learning/"+ next_id+ "'><button class='next-button-start'><span class='next-button-wrapper'>  "+next_topic+"  </span></button></a>")
    }
    else{
        $("#next-button").html("<a href='/quiz/1'><button class='next-button-start'><span class='next-button-wrapper'>  Test  </span></button></a>")
    }

    if(previous_topic != null){
        $("#previous-button").html("<a href='/learning/"+ previous_id+ "'><button class='next-button-start'><span class='next-button-wrapper'>  "+previous_topic+"  </span></button></a>")
    }
})