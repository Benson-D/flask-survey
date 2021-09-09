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
    """Open the survey, retrieve title, and instructions"""

    title = survey.title 
    instructions = survey.instructions

    return render_template('/survey_start.html', title=title, instructions=instructions)

@app.post('/begin')
def show_questions():
    """Redirect user to first question"""

    return redirect('/questions/0')


@app.get('/questions/<int:question>')
def questions_pages(question):

    """Load up survey.questions, display the choices for answers, each havin a radio button"""
    #breakpoint()

    return render_template('/question.html', question=survey.questions[question]) 


@app.post('/answer')
def handle_answers():
    """Append answer to response lst, redirect to next question route, else completion route"""
    
    # Get value from form in question.html, append to responses
    form_answer = request.form["answer"]
    responses.append(form_answer)

    # Variables to compare if equal len
    question_number = len(responses)
    survey_length = len(survey.questions)

    # Need to redirect /answer to next question,
    # Reconfigure questions_pages dynamically
    # Need to away to compare to allow for redirection
    # If no more response redirect to /completion

    if (question_number < survey_length ):
        return redirect(f"/questions/{question_number}")
    else: 
        return redirect('/completion')
    #breakpoint()

@app.get('/completion')
def completed_survey():
    """When survey finished render to completion.html"""
    return render_template('completion.html')

