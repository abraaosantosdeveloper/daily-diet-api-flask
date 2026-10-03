from flask import Flask
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "segredo123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello!"

if __name__ == '__main__':
    from model.User import User
    from model.Meal import Meal

    with app.app_context():
        db.create_all()
    app.run(debug=True)