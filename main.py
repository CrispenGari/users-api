from app import db, app
from blueprints.user import blueprint as user
from blueprints.todo import blueprint as todo

app.register_blueprint(user, url_prefix="/users")
app.register_blueprint(todo, url_prefix="/todos")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=1234, debug=True)
