import json
from flask import Flask, abort
import redis

app = Flask(__name__)
CORS(app)

r = redis.StrictRedis(host="redis")#redis


def get(key):
    value = r.get(key)
    if value is None:
        r.set(key, "")
        return []
    else:
        return str(value)[2:-1].split(" ")[1:]


@app.route('/')
def hello_world():
    return 'It works'

@app.route('/face/image/<imagename>', methods=["GET"])
def get_face_by_image(imagename):
    faces = get(imagename)
    if faces is None:
        abort(404)

    return str(faces)

@app.route('/face/user/<userid>', methods=["GET"])
def get_face_by_user(userid):
    faces = get(userid)
    if faces is None:
        abort(404)

    return str(faces)

app.run(host= 'face-api', port=5000)