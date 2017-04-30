import json
from flask import Flask, abort
import redis

app = Flask(__name__)

r = redis.StrictRedis(host="192.168.99.100")#redis


def get(key):
    return json(str(r.get(key)).split(" ")[1:])

@app.route('/')
def hello_world():
    return 'It works'

@app.route('/face/image/<imagename>', methods=["GET"])
def get_face_by_image(imagename):
    faces = get(imagename)
    if faces is None:
        abort(404)

    return faces

@app.route('/face/user/<userid>', methods=["GET"])
def get_face_by_image(userid):
    faces = get(userid)
    if faces is None:
        abort(404)

    return faces

