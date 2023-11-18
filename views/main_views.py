from flask import Blueprint, render_template, url_for
from src.models import Question
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():

    return render_template('index.html')

@bp.route('/post/')
def post():
    question_list = Question.query.order_by(Question.create_date.desc())
    return redirect(url_for('question.post'))
