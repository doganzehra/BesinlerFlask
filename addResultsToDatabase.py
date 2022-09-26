import firebase_admin
from firebase_admin import credentials, firestore


firestoreDb2 = firestore.client()

snapshots = list(firestoreDb2.collection(u'user_foods').get())


def saveResultsToDatabase(uid, date, semptom, resultDict):
    resultList = resultDict.items()

    for value in resultList:
        print('savemetodu')
        if controlDuplicates(uid, value, semptom) == True:
            firestoreDb2.collection(u'user_results').add(
                {'uid': uid, 'date': date, 'symptom': semptom, 'result_name': value})
            print('savemetodu eklendi')


def controlDuplicates(uid, value, semptom):
    snapshots = list(firestoreDb2.collection(u'user_results').get())

    for snap in snapshots:
        if snap.to_dict()['uid'] == uid:
            print(value)
            print('--------')
            print(snap.to_dict()['result_name'])
            if snap.to_dict()['result_name'] == value:
                if snap.to_dict()['symptom'] == semptom:
                    return False
    return True
