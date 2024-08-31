from firebase import firebase
from firebase import auth

email = "clarkr30@gmail.com"
user = auth.get_user_by_email(email)

fb = firebase.FirebaseApplication('https://console.firebase.google.com/u/0/project/plantmonitor-19a40/database/plantmonitor-19a40-default-rtdb/data/~2F', None)
Result = fb.post('test/coffee', {'percentage': 40})