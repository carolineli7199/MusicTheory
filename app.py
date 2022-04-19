from flask import Flask
from flask import render_template, redirect, url_for
from flask import Response, request, jsonify

app = Flask(__name__)
learning_data = {
    "1": {
        "id": 1,
        "num_blurbs": 1,
        "title": "The Staff",
        "info": [
            "The backbone of reading music starts with <b>the staff</b>. The staff and the bass (covered next) will be how you determine notes.",
        ],
        "num_imgs": 1,
        "imgs": [
            "http://bp3.blogger.com/_Tad4UOfdqXs/RZTwOqb7whI/AAAAAAAAAAc/A31QI-ZldAM/w1200-h630-p-k-no-nu/staff-2.jpg",
        ],
        "next": "The Clefs"
    },
    "2": {
        "id": 2,
        "num_blurbs": 1,
        "title": "The Clefs",
        "info": [
            "Music has two clefs: the <b>treble</b> and <b>bass</b> clefs. In music theory, each clef is denoted on the left side of the staff.",
        ],
        "num_imgs": 2,
        "imgs": [
            "https://www.liveabout.com/thmb/zpDIbDJxet6iSIuiAPmpTdcnueo=/1780x1096/filters:no_upscale():max_bytes(150000):strip_icc()/treble-304441_1280_-5c8721fbc9e77c00010c2285.jpg",
            "https://hellomusictheory.com/wp-content/uploads/2019/04/bass-clef-1024x682.png",
        ],
        "next": "Middle C"
    },
    "3": {
        "id": 3,
        "num_blurbs": 1,
        "title": "Middle C",
        "info": [
            "The easiest way to start reading notes is by using a “home base”. It often is the “middle” C note. It is denoted with the line in the middle to show that it is a note on a line in the staff. <br>Notes always repeat in A-G order and wrap around. So, once you have C you can count up or down to the note you desire."
        ],
        "num_imgs": 2,
        "imgs": [
            "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-middle-C.jpg",
            "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Bass-Clef-Notes-Quiz-Middle-C.jpg",
        ],
        "next": "Treble Spaces and Lines"
    },
    "4": {
        "id": 4,
        "num_blurbs": 2,
        "title": "Treble Spaces and Lines",
        "info": [
            "On the treble clef the notes in the spaces will spell out F-A-C-E in ascending order.",
            "On the treble clef the notes on the lines will spell out E-G-B-D-F in ascending order.",
        ],
        "num_imgs": 2,
        "imgs": [
            "https://www.musictheoryacademy.com/wp-content/uploads/2011/02/treble-clef-spaces.jpg",
            "https://www.musictheoryacademy.com/wp-content/uploads/2011/02/music-theory-treble-clef-lines2.jpg",
        ],
        "next": "Clef Spaces and Lines"
    },
    "5": {
        "id": 5,
        "num_blurbs": 3,
        "title": "Clef Spaces and Lines",
        "info": [
            "On the bass clef the notes in the spaces will spell out A-C-E-G in ascending order.",
            "On the bass clef the notes on the lines will spell out G-B-D-F-A in ascending order.",
            "Notice: compared to the treble, each note was essentially shifted down one on the staff.",
        ],
        "num_imgs": 2,
        "imgs": [
            "https://www.skoove.com/blog/wp-content/uploads/2019/08/Space-Notes-1024x492.png",
            "https://www.kindpng.com/picc/m/303-3034242_bass-line-notes-bass-clef-note-f-hd.png",
        ],
        "next": "Example"
    },
    "6": {
        "id": 6,
        "num_blurbs": 1,
        "title": "Example",
        "info": [
            "From middle C, we would count up to: D, E, F, G. So this note is G."
        ],
        "num_imgs": 1,
        "imgs": [
            "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-G.jpg"
        ],
        "next": None
    }
}
quiz_data = {
    "1": {
        "id": 1,
        "type": "mc",
        "img": "https://www.musictheoryacademy.com/wp-content/uploads/2020/06/Treble-Clef-Notes-Quiz-G.jpg",
        "correct": "G", # index of the correct answer
        "options": [
            "A",
            "B",
            "D",
            "G",
            "F"
        ],
        "end_flag": 0
    },
    "2": {
        "id": 2,
        "type": "mc",
        "img": "https://www.quiz-tree.com/images/Music/bass_clef_staff_F3_600x393.png",
        "correct": "F",
        "options": [
            "C",
            "F",
            "A",
            "G",
            "E"
        ],
        "end_flag": 1
    }
}

NUM_QUIZ_QUESTIONS = len(quiz_data)
num_correct_answer = 0


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')   
    #return "hello world"

@app.route('/learning/<id>')
def loadLearningPage(id=None):
    return render_template('learn.html', learning_data=learning_data[id])  # implement

@app.route('/quiz/<id>')
def loadQuizPage(id=None):
    return render_template('quiz.html', quiz_data=quiz_data[id])  # implement

@app.route('/quizend')
def loadQuizEndPage(id=None):
    global num_correct_answer
    correct_counts = num_correct_answer
    num_correct_answer = 0
    return render_template('end.html', num=correct_counts, total=NUM_QUIZ_QUESTIONS) 

@app.route('/quiz/checkanswer', methods=['GET', 'POST'])
def checkanswer():
    global num_correct_answer
    json_data = request.get_json()   
    user_answer = json_data["user_answer"] 
    quiz_id = json_data["quiz_id"]
    print(quiz_data[quiz_id]["correct"] )
    print(user_answer)
    if quiz_data[quiz_id]["correct"] == user_answer:
        num_correct_answer += 1
        return jsonify(notice = "Correct")
    return jsonify(notice = "Wrong")


if __name__ == '__main__':
    app.run(debug=True)
