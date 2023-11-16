from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/') # url_prefix는 함수의 애너테이션 url 앞에 기본값으로 붙일 접두어이다.

@bp.route('/')

def index():

    return render_template('index.html')

@bp.route('/login')
def login():

    return render_template('login.html')



