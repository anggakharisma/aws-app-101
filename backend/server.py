from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

from pymongo import MongoClient
import jwt
import os
import bcrypt

load_dotenv()

client = MongoClient()
db = client['aws_101']

app = Flask(__name__)
CORS(app)

@app.post("/login")
def login():
    try:
        content = request.json
        user = db['users'].find_one({ 
            'email': content['email']
        })

        if user == None:
            return jsonify({
                "message": 'User or password might be wrong'
            }), 404

        # incoming password
        request_password = content['password'].encode('utf-8')
        request_hashed =  bcrypt.hashpw(request_password, bcrypt.gensalt())
        result = bcrypt.checkpw(request_password,
                                user['password'].encode('utf-8'))

        if result == False:
            return jsonify({
                "message": 'User or password might be wrong'
            }), 404

        token = jwt.encode({
            "email": content['email'],
        }, os.getenv('JWT_SECRET'), algorithm='HS256')

        return jsonify({
            'email': content['email'],
            'token': token
        }), 200
    except Exception as e:
        print(str(e))
        return jsonify({
            'message': 'Something went wrong',
        }), 500

@app.route("/")
def index():
    return {
        'message': 'aws-101-assesment-angga'
    }

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('PORT') if True else 8080, debug=True)
