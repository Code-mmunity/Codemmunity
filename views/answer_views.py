from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from app import db
from src.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']
    get_ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    answer = Answer(content=content, create_date=datetime.now(), ip=get_ip)
    question.answer_set.append(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))