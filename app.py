from flask import Flask, request, session, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)
questions = satisfaction_survey.questions


@app.route('/')
def show_homepage():
    """ displays title of survey, instructions, and button to start survey """
    session['response'] = []

    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template('/home_page.html', title=title, instructions=instructions)

@app.route('/', methods=["POST"])
def redirect_homepage():
    return redirect(f'/questions/0')

@app.route('/questions/<int:number>', methods=["POST"])
def redirect_questionpage(number):

    next_route = f'/questions/{number}'
    return redirect(next_route)


@app.route('/questions/<int:number>', methods=["GET"])
def show_questionpage(number):
    """save the previous response in session if not page 0, then show current question/form"""

    title = satisfaction_survey.title
    current_question = questions[number]

    # Figure out the next question's number
    next_page = number + 1
    next_route = f'/questions/{next_page}'

    return render_template('question_page.html', next_route=next_route, title=title, current_question=current_question)
