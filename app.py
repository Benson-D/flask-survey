from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []
# push satisfaction_survey.questions[question].choices into response lst

#/questions/0


@app.get('/')
def start_survey(): 
    """Open the survey, retrieve survey.title, and survey.instructions"""
    title = survey.title 
    instructions = survey.instructions

    return render_template('/survey_start.html', title=title, instructions=instructions)

@app.get('/questions/<question>')
def questions_pages(question):

    """Set up docstring"""

    return '' 