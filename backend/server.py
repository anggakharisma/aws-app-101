from dotenv import load_dotenv
from flask import Flask, request, jsonify

from pymongo import MongoClient
import jwt
import os
import bcrypt

load_dotenv()

client = MongoClient()
db = client['aws_101']

app = Flask(__name__)
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
        salt = bcrypt.gensalt()
        request_passwod = content['password'].encode('utf-8')
        request_hashed =  bcrypt.hashpw(request_passwod, salt)
        result = bcrypt.checkpw(content['password'].encode('utf-8'),
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
