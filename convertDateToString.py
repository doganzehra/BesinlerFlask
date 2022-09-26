import time
import firebase_admin
from firebase_admin import credentials, firestore


def convertDateToString(date):
    date_time = date.strftime("%Y-%m-%d %H:%M:%S+00:00")
    return date_time
