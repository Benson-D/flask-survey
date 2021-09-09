from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

# old method before step 6
# responses = []
# push satisfaction_survey.questions[question].choices into response lst

#/questions/0


@app.get('/')
def start_survey(): 
    """Open the survey, retrieve title, and instructions from survey class"""

    title = survey.title 
    instructions = survey.instructions

    session['responses'] = []

    return render_template('/survey_start.html', title=title, instructions=instructions)

@app.post('/begin')
def show_questions():
    """Redirect user to first question after hitting start survey"""

    return redirect('/questions/0')


@app.get('/questions/<int:question>')
def questions_pages(question):
    """Load up survey.questions, display the choices for answers, each having a radio button"""

    #breakpoint()
    # question < response length or question > response length
    # redirect to the response length question page
    #   accessing /2 when response length = 0, send user back to page /0 
    # otherwise, should be on the correct page
    # e.g. /2 == response length of 2; means they're on the 3rd question which corresponds to /2

    check_response = len(session['responses'])

    if(question < check_response or question > check_response):
        flash('Please answer this question before moving on!')
        return redirect(f'/questions/{check_response}')

    return render_template('/question.html', question=survey.questions[question]) 


@app.post('/answer')
def handle_answers():
    """Append answer to response lst, redirect to next question route, else completion route"""
    
    # previous method before step 6
    # Get value from form in question.html, append to responses
    # form_answer = request.form["answer"]
    # responses.append(form_answer)

    form_answer = request.form['answer']
    responses = session['responses']
    responses.append(form_answer)
    session['responses'] = responses

    # Variables to compare if equal len

    # question: what would be best practice so we don't repeat line 72 and 46
    question_number = len(session['responses'])
    survey_length = len(survey.questions)

    # breakpoint()
    # Need to redirect /answer to next question,
    # Reconfigure questions_pages dynamically
    # Need to away to compare to allow for redirection
    # If no more response redirect to /completion

    if (question_number < survey_length ):
        return redirect(f'/questions/{question_number}')
    else: 
        return redirect('/completion')
    #breakpoint()

@app.get('/completion')
def completed_survey():
    """When survey finished render completion page"""
    return render_template('completion.html')
