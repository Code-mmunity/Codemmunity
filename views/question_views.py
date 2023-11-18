from flask import Blueprint, render_template, request, url_for
from datetime import datetime
from flask import request
from src.models import Question
from src.forms import QuestionForm, AnswerForm
from werkzeug.utils import redirect
from app import db

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/post/')
def post():

    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())

    question_list = question_list.paginate(page=page, per_page=20)

    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/post/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('question.post'))
    return render_template('question/question_form.html', form=form)