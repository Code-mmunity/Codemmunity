from flask import Blueprint, render_template
from flask import request
from src.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/post/')
def post():

    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())

    question_list = question_list.paginate(page=page, per_page=20)

    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/post/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)