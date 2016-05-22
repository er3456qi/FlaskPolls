from polls import app, db
from .models import Question
from flask import render_template, abort, redirect, request, url_for


@app.route('/')
def index():
    latest_question_list = Question.query.order_by('pub_date')[:5]
    return render_template('index.html', latest_question_list=latest_question_list)


@app.route('/detail/<int:question_id>')
def detail(question_id):
    question = Question.query.get(question_id)
    if question is None:
        abort(404)
    return render_template('detail.html', question=question)


@app.route('/results/<int:question_id>')
def results(question_id):
    question = Question.query.get(question_id)
    if question is None:
        abort(404)
    return render_template('results.html', question=question)


@app.route('/vote/<int:question_id>', methods=['POST'])
def vote(question_id):
    question = Question.query.get(question_id)
    try:
        choice_id = int(request.form['choice'])
        selected_choice = [c for c in question.choice_set if c.id == choice_id][0]
    except IndexError:
        return render_template('detail.html',
                               question=question,
                               error_message="you didn't select a choice."
                               )
    else:
        selected_choice.votes += 1
        db.session.add(selected_choice)
        db.session.commit()
        return redirect(url_for('results', question_id=question.id))