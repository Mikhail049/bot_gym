import mysql.connector
import pprint
import os
from datetime import datetime


def connectionToDb():
    return mysql.connector.connect(user = os.getenv("USER_NAME_MYSQL"),
                              password= os.getenv("PASS_MYSQL"),
                              host= os.getenv("MYSQL_HOST"),
                              database=os.getenv("DB_NAME_MYGYM"))


def getNameExcercise(exerciseName):
    commandString = 'Select * From dt_mapping_exercises WHERE input_name_exercise=%s'
    data = (exerciseName)
    cnx = connectionToDb()
    cursor = cnx.cursor()
    cursor.execute(commandString)
    result = cursor.fetchall()
    cnx.close()
    pprint.pprint(result)
    return result


def addExerciseToStack(user, exercise, reps, minutes, weight):
    commandS = "INSERT INTO dt_mapping_exercises (user, exercise, date, reps, minutes, weight) " \
               "VALUE(%s, %s, %s, %s);"
    data = (user, exercise, datetime.now(), reps, minutes, weight)
    cnx = connectionToDb()
    cursor = cnx.cursor()
    cursor.execute(commandS, data)
    cnx.close()


def addUserToDB():
    commandString = 'Select * From dt_mapping_exercises'
    cnx = connectionToDb()
    cursor = cnx.cursor()
    cursor.execute(commandString)
    result = cursor.fetchall()
    cnx.close()

    pprint.pprint(result)
