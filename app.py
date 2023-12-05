from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
from flask_admin import Admin
from sqlalchemy import MetaData
from flask_admin.contrib.sqla import ModelView

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def page_not_found(e):

    return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # adminPage
    # set flask_admin (/admin 경로로 이동하면 admin 정보 출력)
    admin = Admin(app, name='Codemmunity', template_mode='bootstrap3')



    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    # 여기서 views/main_views를 임포트합니다.
    from views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    from src.filter import format_datetime

    app.jinja_env.filters['datetime'] = format_datetime

    # 오류 페이지
    app.register_error_handler(404, page_not_found)

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5027, debug=True, ssl_context='adhoc')