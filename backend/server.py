from dotenv import load_dotenv
from flask import Flask, request, jsonify

from pymongo import MongoClient
import jwt
import os

load_dotenv()

client = MongoClient()
db = client['aws-101']

app = Flask(__name__)
@app.post("/login")
def login():
    try:
        content = request.json

        token = jwt.encode({
            "email": content['email'],
        }, os.getenv('JWT_SECRET'), algorithm='HS256')

        return jsonify({
            'email': content['email'],
            'token': token
        }), 200
    except:
        return jsonify({
            'message': 'Something went wrong'
        }), 500

@app.route("/")
def index():
    return {
        'message': 'aws-101-assesment-angga'
    }

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('PORT') if True else 8080, debug=True)
