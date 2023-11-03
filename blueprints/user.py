from flask import Blueprint, request, jsonify, make_response
from models import User
from app import db

blueprint = Blueprint("user", __name__)


@blueprint.route("/edit/<int:id>", methods=["POST", "GET", "PATCH", "PUT", "DELETE"])
def update(id):
    if request.method == "PUT" or request.method == "PATCH":
        user = User.query.filter_by(id=id).first()
        if not user:
            return (
                make_response(
                    jsonify(
                        {
                            "method": request.method,
                            "status": "NOT FOUND",
                            "code": 404,
                            "error": f"The user of id '{id}' does not exists.",
                        }
                    )
                ),
                404,
            )
        if request.is_json:
            try:
                json_data = request.get_json()
                data = {
                    "name": json_data.get("name"),
                    "email": json_data.get("email"),
                    "gender": json_data.get("gender"),
                    "surname": json_data.get("surname"),
                }
                user.name = data["name"] if data["name"] else user["name"]
                user.email = data["email"] if data["email"] else user["email"]
                user.gender = data["gender"] if data["gender"] else user["gender"]
                user.surname = data["surname"] if data["surname"] else user["surname"]
                db.session.commit()
                return make_response(jsonify(user.json())), 204
            except Exception as e:
                return (
                    make_response(
                        jsonify({"error": "The email address must be unique"})
                    ),
                    200,
                )
        else:
            return (
                make_response(
                    jsonify(
                        {
                            "method": request.method,
                            "status": "INTERNAL SERVER ERROR",
                            "code": 500,
                            "error": "You should pass json data with this request.",
                        }
                    )
                ),
                500,
            )
    return (
        make_response(
            jsonify(
                {
                    "method": request.method,
                    "status": "METHOD NOT ALLOWED",
                    "code": 405,
                    "error": "The request method must be post or patch method only on this route",
                }
            )
        ),
        405,
    )


@blueprint.route("/add", methods=["POST", "GET", "PATCH", "PUT", "DELETE"])
def add():
    if request.method == "POST":
        if request.is_json:
            json_data = request.get_json()
            try:
                user = User(
                    json_data.get("name"),
                    json_data.get("email"),
                    json_data.get("gender"),
                    json_data.get("surname"),
                )
                db.session.add(user)
                db.session.commit()
                return make_response(jsonify(user.json())), 201
            except Exception as e:
                return (
                    make_response(
                        jsonify({"error": "The email address must be unique"})
                    ),
                    200,
                )
        else:
            return (
                make_response(
                    jsonify(
                        {
                            "method": request.method,
                            "status": "INTERNAL SERVER ERROR",
                            "code": 500,
                            "error": "You should pass json data with this request.",
                        }
                    )
                ),
                500,
            )
    return (
        make_response(
            jsonify(
                {
                    "method": request.method,
                    "status": "METHOD NOT ALLOWED",
                    "code": 405,
                    "error": "The request method must be get method only on this route",
                }
            )
        ),
        405,
    )


@blueprint.route("/all", methods=["POST", "GET", "PATCH", "PUT", "DELETE"])
def all():
    if request.method == "GET":
        users = User.query.all()
        return (
            make_response(jsonify([user.json() for user in users])),
            200,
        )
    return (
        make_response(
            jsonify(
                {
                    "method": request.method,
                    "status": "METHOD NOT ALLOWED",
                    "code": 405,
                    "error": "The request method must be get method only on this route",
                }
            )
        ),
        405,
    )


@blueprint.route("/one/<int:id>", methods=["POST", "GET", "PATCH", "PUT", "DELETE"])
def one(id):
    if request.method == "GET":
        user = User.query.filter_by(id=id).first()
        if not user:
            return (
                make_response(
                    jsonify(
                        {
                            "method": request.method,
                            "status": "NOT FOUND",
                            "code": 404,
                            "error": f"The user of id '{id}' does not exists.",
                        }
                    )
                ),
                404,
            )
        else:
            return (
                make_response(jsonify(user.json())),
                200,
            )
    return (
        make_response(
            jsonify(
                {
                    "method": request.method,
                    "status": "METHOD NOT ALLOWED",
                    "code": 405,
                    "error": "The request method must be get method only on this route",
                }
            )
        ),
        405,
    )


@blueprint.route("/delete/<int:id>", methods=["POST", "GET", "PATCH", "PUT", "DELETE"])
def delete(id):
    global users
    if request.method == "DELETE":
        user = User.query.filter_by(id=id).first()
        if not user:
            return (
                make_response(
                    jsonify(
                        {
                            "method": request.method,
                            "status": "NOT FOUND",
                            "code": 404,
                            "error": f"The user of id '{id}' does not exists.",
                        }
                    )
                ),
                404,
            )
        else:
            db.session.delete(user)
            db.session.commit()
            return (
                make_response(jsonify({"message": "User has been deleted!"})),
                204,
            )
    return (
        make_response(
            jsonify(
                {
                    "method": request.method,
                    "status": "METHOD NOT ALLOWED",
                    "code": 405,
                    "error": "The request method must be get method only on this route",
                }
            )
        ),
        405,
    )
