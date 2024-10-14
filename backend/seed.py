import pymongo
import bcrypt
from dotenv import load_dotenv

client = pymongo.MongoClient()
db = client['aws_101']

p = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt())

db['users'].create_index([("email", pymongo.ASCENDING)], unique=True)

db.users.insert_one({
        'name': 'User test',
        'email': 'admin@test.com',
        'password': p.decode('utf-8')
    })
