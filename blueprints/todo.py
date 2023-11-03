from flask import Blueprint, request, jsonify, make_response

blueprint = Blueprint("todo", __name__)

todos = []


@blueprint.route("/all", methods=["POST", "GET", "PATCH", "PUT", "DELETE"])
def all():
    if request.method == "GET":
        return (
            make_response(jsonify(todos)),
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
