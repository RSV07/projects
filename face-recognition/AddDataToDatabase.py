import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-6eaf0-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "733023":
        {
            "name": "Rishik",
            "major": "cse",
            "starting_year":2017,
            "total_attendance":6,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2023-01-10 00:54:34"

        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "cse",
            "starting_year":2017,
            "total_attendance":3,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-01-10 00:54:34"

        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "cse",
            "starting_year":2017,
            "total_attendance":1,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2020-01-10 00:54:34"

        },
    "733014":
        {
            "name": "Vedanth",
            "major": "cse",
            "starting_year":2017,
            "total_attendance":1,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2020-01-10 00:54:34"

        },
    "000001":
        {
            "name": "Padmasri",
            "major": "cse",
            "starting_year":2017,
            "total_attendance":3,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-01-10 00:54:34"
        },
    "733036":
        {
            "name": "ansh",
            "major": "cse",
            "starting_year":2017,
            "total_attendance":3,
            "standing": "G",
            "year":4,
            "last_attendance_time": "2022-01-10 00:54:34"

        }

}

for key, value in data.items():
    ref.child(key).set(value)