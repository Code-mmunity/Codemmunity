from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # 여기서 views/main_views를 임포트합니다.
    from views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    from src.filter import format_datetime

    app.jinja_env.filters['datetime'] = format_datetime

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5027, debug=True)