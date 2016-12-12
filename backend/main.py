import flask

from app import create_app
from app import models


app = create_app()


@app.route("/api/request", methods=['POST', 'GET'])
def save_request():
    user_ip = flask.request.headers.get("X-Real-IP")
    if flask.request.method == 'POST':
        user_request = models.UserRequest(user_ip=user_ip)
        user_request.save()
        response, status = 'OK', 201
    else:
        response = models.UserRequest.query.filter(
            models.UserRequest.user_ip==user_ip).all()
        response = {'ip': user_ip,
                    'requests': [resp.created_at for resp in response]}
        response, status = flask.jsonify(response), 200
    return response, status


if __name__ == "__main__":
    app.run(host='0.0.0.0')
