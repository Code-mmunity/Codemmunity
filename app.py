from flask import Flask, render_template
from views import main_view
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

app.register_blueprint(main_view.bp)

# ORM

db.init_app(app)
migrate.init_app(app, db)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
