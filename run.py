from flask import Flask
from flask_migrate import Migrate
from settings import DevSettings
from database import db
from api.category_api import category_bp
from api.question_api import question_bp
from api.answer_api import answer_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevSettings)
    db.init_app(app)
    Migrate(app, db)
    app.register_blueprint(category_bp, url_prefix="/categories")
    app.register_blueprint(question_bp, url_prefix="/questions")
    app.register_blueprint(answer_bp, url_prefix="/answers")
    return app

if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(debug=True)
