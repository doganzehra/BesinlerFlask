import json
import numpy as np
import pandas as pd
import string
import random
from flask import Flask, Response, jsonify, request
import csv
from datetime import date

from unidecode import unidecode
from apriori import getAprioriResult
from getUserFoodsFromDatabase import getUserFoods
from controlDBandResults import controlResults
from addResultsToDatabase import saveResultsToDatabase
from convertDateToString import convertDateToString
import csv

app = Flask(__name__)


@app.route('/getResult', methods=['GET'])
def recommendSongs():
    args = request.args
    uid = args['uid']
    date = args['date']
    semptom = args['semptom']
    resultAprioriDict = getAprioriResult(semptom)
    print(resultAprioriDict)
    print('REQUEST TARİHİ: ' + date)
    resultListFromDB = getUserFoods(uid, date)
    print(resultListFromDB)
    resultFinallyDict = controlResults(resultAprioriDict, resultListFromDB)
    print(resultFinallyDict)
    saveResultsToDatabase(uid, date, semptom, resultFinallyDict)
    return jsonify('basarılı')


@app.route('/saveToDataset', methods=['GET'])
def saveSympthom():

    args = request.args
    uid = args['uid']
    date = args['date']
    semptom = args['semptom']
    foods = getUserFoods(uid, date)
    foods = ['armut', 'avokado', 'soğan', 'lahana', 'yumurta', 'salam', '', 'tuz', 'soğuk çay', 'çilek', 'ekmek', 'tavuk eti', 'margarin', 'ananas',
             'seker', 'domates', 'bitki çayı', 'kajun', 'ıspanak', 'muz', 'buğday', 'nar', 'boza', 'marul', 'sarımsak', 'salatalık', 'biber', 'maydanoz']
    semptom = semptom + '.csv'
    with open(semptom, 'a') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(foods)


if __name__ == '__main__':
    app.run(port=5000)
