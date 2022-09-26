import json
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

from pandas import DateOffset
from convertDateToString import convertDateToString

dbinfo = credentials.Certificate("projeJson.json")
firebase_admin.initialize_app(dbinfo)

firestoreDb = firestore.client()

snapshots = list(firestoreDb.collection(u'user_foods').get())


def getUserFoods(uid, date):
    myList = []
    snapshots = list(firestoreDb.collection(u'user_foods').get())
    for snap in snapshots:
        if snap.to_dict()['uid'] == uid:
            date2 = convertDateToString(snap.to_dict()['date'])
            print(date2)
            if date2 == date:
                myList.append(snap.to_dict()['food_name'])
    return myList
