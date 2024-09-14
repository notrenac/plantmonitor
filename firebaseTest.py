import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import glob

cred = credentials.Certificate(glob.glob("keys/*.json")[0])
firebase_admin.initialize_app(cred, {'databaseURL': 'https://plantmonitor-19a40-default-rtdb.firebaseio.com'})
# firebase_admin.initialize_app(cred)
ref = db.reference("/")

with open("test.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
