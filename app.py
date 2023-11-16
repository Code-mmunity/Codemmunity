from flask import Flask, render_template
from views import main_view
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import IPAddressType

import config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

app.config.from_object(config) # config.py에 작성한 항목 app.config를 환경변수로 부르기 위함

app.register_blueprint(main_view.bp)

# ORM

from src import models

db.init_app(app) # 초기화
migrate.init_app(app, db) # 초기화


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
