from flask import Flask

from app import app, db
from blueprints.user import blueprint as user
from blueprints.todo import blueprint as todo


class Config:
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 1234


@app.route("/", methods=["GET", "POST"])
def hi():
    return "Hi there", 200


app.register_blueprint(user, url_prefix="/users")
app.register_blueprint(todo, url_prefix="/todos")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG, use_reloader=False)
