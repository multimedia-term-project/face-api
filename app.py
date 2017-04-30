import json
from flask import Flask
import redis

app = Flask(__name__)

r = redis.StrictRedis(host="192.168.99.100")#redis


def get(key):
    return json(str(r.get(key)).split(" ")[1:])

@app.route('/')
def hello_world():
    return 'It works'

