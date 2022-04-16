from flask import Flask
from flask import render_template, redirect, url_for
from flask import Response, request, jsonify

app = Flask(__name__)

NUM_QUIZ_QUESTIONS = 10
num_correct_answer = 0
data = {}


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')   
    #return "hello world"

@app.route('/learning/<id>')
def loadLearningPage(id=None):
    return render_template('learn.html', id=id)  # implement

@app.route('/quiz/<id>')
def loadQuizPage(id=None):
    return render_template('quiz.html', id=id)  # implement

@app.route('/quizend')
def loadQuizEndPage(id=None):
    return render_template('end.html', num=num_correct_answer, total=NUM_QUIZ_QUESTIONS) 

if __name__ == '__main__':
    app.run(debug=True)
