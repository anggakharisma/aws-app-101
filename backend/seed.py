import pymongo
import bcrypt
import os
from dotenv import load_dotenv

from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_HOST"))
db = client['aws_101']

p = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())

db['users'].create_index([("email", pymongo.ASCENDING)], unique=True)

db.users.insert_one({
        'name': 'User test',
        'email': 'admin@test.com',
        'password': p.decode('utf-8')
    })
