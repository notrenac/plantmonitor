import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

cred = credentials.Certificate('plantmonitor-19a40-firebase-adminsdk-8b656-f5000f8953.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://plantmonitor-19a40-default-rtdb.firebaseio.com'})
# firebase_admin.initialize_app(cred)
ref = db.reference("/")

with open("test.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
