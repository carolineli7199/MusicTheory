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
        "staff": {
            "clef": 0,
            "notes": []
        },
        "next": "The Clefs",
        "previous": None
    },
    "2": {
        "id": 2,
        "num_blurbs": 1,
        "title": "The Clefs",
        "info": [
            "Music has two clefs: the <b>treble</b> and <b>bass</b> clefs. In music theory, each clef is denoted on the left side of the staff.",
        ],
        "num_imgs": 2,
        "staff": [
            {
                "clef": 1,
                "notes": []
            },
            {
                "clef": 2,
                "notes": []
            }
        ],
        "next": "Middle C",
        "previous": "The Staff"
    },
    "3": {
        "id": 3,
        "num_blurbs": 1,
        "title": "Middle C",
        "info": [
            "The easiest way to start reading notes is by using a “home base”. It often is the “middle” C note. It is denoted with the line in the middle to show that it is a note on a line in the staff.",
            "Notes always repeat in A-G order and wrap around. So, once you have C you can count up or down to the note you desire."
        ],
        "num_imgs": 2,
        "staff": [
            {
                "clef": 1,
                "notes": [
                    {"keys": ["c/4"]}
                ]
            },
            {
                "clef": 2,
                "notes": [
                    {"keys": ["a/5"]}
                ]
            }
        ],
        "next": "Treble Spaces and Lines",
        "previous": "The Clefs"
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
        "staff": [
            {
                "clef": 1,
                "notes": [
                    {"keys": ["f/4"]},
                    {"keys": ["a/4"]},
                    {"keys": ["c/5"]},
                    {"keys": ["e/5"]}
                ]
            },
            {
                "clef": 1,
                "notes": [
                    {"keys": ["e/4"]},
                    {"keys": ["g/4"]},
                    {"keys": ["b/4"]},
                    {"keys": ["d/5"]},
                    {"keys": ["f/5"]},
                ]
            }
        ],
        "next": "Clef Spaces and Lines",
        "previous": "Middle C"
        
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
        "staff": [
            {
                "clef": 2,
                "notes": [
                    {"keys": ["f/4"]},
                    {"keys": ["a/4"]},
                    {"keys": ["c/5"]},
                    {"keys": ["e/5"]}
                ]
            },
            {
                "clef": 2,
                "notes": [
                    {"keys": ["e/4"]},
                    {"keys": ["g/4"]},
                    {"keys": ["b/4"]},
                    {"keys": ["d/5"]},
                    {"keys": ["f/5"]},
                ]
            }
        ],
        "next": "Example",
        "previous": "Treble Spaces and Lines"
        
    },
    "6": {
        "id": 6,
        "num_blurbs": 1,
        "title": "Example",
        "info": [
            "From middle C, we would count up to: D, E, F, G. So this note is G."
        ],
        "num_imgs": 1,
        "staff": {
            "clef": 1,
            "notes": [
                {"keys": ["c/4"]},
                {"keys": ["g/4"]}
            ]
        },
        "next": None,
        "previous": "Clef Spaces and Lines"
    }
}
quiz_data = {
     "1": {
        "id": 1,
        "type": "mc",
        "question": "What is the name of the following clef?",
        "staff": {
            "clef": 1,
            "notes": []
        },
        "correct": "C",
        "options": [
            "A",
            "B",
            "C"
        ],
        "has_contents": 1,
        "contents": [
            "Clef",
            "Bass",
            "treble"
        ],
        "end_flag": 0
    },
     "2": {
        "id": 2,
        "type": "mc",
        "question": "Is this Bass clef correctly placed?",
        "staff": {
            "clef": 2,
            "notes": []
        },
        "correct": "Yes",
        "options": [
            "Yes",
            "No"
        ],
        "has_contents": 0,
        "contents": ['', ''],
        "end_flag": 0
    },
    "3": {
        "id": 3,
        "type": "mc",
        "question": "Which note is placed on the staff?",
        "staff": {
            "clef": 1,
            "notes": [
                {"keys": ["g/4"]}
            ]
        },
        "correct": "G",
        "options": [
            "A",
            "B",
            "D",
            "G",
            "F"
        ],
        "has_contents": 0,
        "contents": ['', ''],
        "end_flag": 0
    },
    "4": {
        "id": 4,
        "type": "mc",
        "question": "Which note is placed on the staff?",
        "staff": {
            "clef": 1,
            "notes": [
                {"keys": ["e/5"]}
            ]
        },
        "correct": "E",
        "options": [
            "A",
            "B",
            "D",
            "E",
            "F"
        ],
        "has_contents": 0,
        "contents": ['', ''],
        "end_flag": 0
    },
    "5": {
        "id": 5,
        "type": "mc",
        "question": "Which note is placed on the staff?",
        "staff": {
            "clef": 2,
            "notes": [
                {"keys": ["f/4"]}
            ]
        },
        "correct": "F",
        "options": [
            "C",
            "F",
            "A",
            "G",
            "E"
        ],
        "has_contents": 0,
        "contents": ['', ''],
        "end_flag": 0
    },
    "6": {
        "id": 6,
        "type": "mc",
        "question": "Which note is placed on the staff?",
        "staff": {
            "clef": 2,
            "notes": [
                {"keys": ["a/4"]}
            ]
        },
        "correct": "A",
        "options": [
            "A",
            "B",
            "D",
            "G",
            "F"
        ],
        "has_contents": 0,
        "contents": ['', ''],
        "end_flag": 0
    },
    "7": {
        "id": 7,
        "type": "clicknode",
        "question": "Given a staff with a treble placed in the beginning, place a note at location that the lower “E” note appears.",
        "staff": {
            "clef": 1,
            "notes": [
                {"keys": ["e/4"]}
            ]
        },
        "correct": "E",
        "end_flag": 0
    },
    "8": {
        "id": 8,
        "type": "clicknode",
        "question": "Given a staff with a treble placed in the beginning, place a note at location that a “D” note appears.",
        "staff": {
            "clef": 1,
            "notes": [
                {"keys": ["d/4"]}
            ]
        },
        "correct": "D",
        "end_flag": 0
    },
    "9": {
        "id": 9,
        "type": "clicknode",
        "question": "Given a staff with a bass placed in the beginning, place a note at location that a “E” note appears.",
        "staff": {
            "clef": 2,
            "notes": [
                {"keys": ["e/4"]}
            ]
        },
        "correct": "E",
        "end_flag": 0
    },
    "10": {
        "id": 10,
        "type": "clicknode",
        "question": "Given a staff with a bass placed in the beginning, place a note at location that a “D” note appears.",
        "staff": {
            "clef": 2,
            "notes": [
                {"keys": ["d/4"]}
            ]
        },
        "correct": "D",
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
    if quiz_id == 1:
        num_correct_answer = 0
    # print(quiz_data[quiz_id]["correct"] )
    # print(user_answer)
    if quiz_data[quiz_id]["correct"] == user_answer:
        num_correct_answer += 1
        print("Correct")
        print(num_correct_answer)
        return jsonify(notice = "Correct")
    print("Wrong")
    print(num_correct_answer)
    return jsonify(notice = "Wrong")

@app.context_processor
def inject_learn_menu():
    global learning_data
    return dict(learning_menu=learning_data)


if __name__ == '__main__':
    app.context_processor(inject_learn_menu)
    app.run(debug=True)
