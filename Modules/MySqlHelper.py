import mysql.connector
import pprint
import os
from datetime import datetime


connectionParameters = {
    'user': os.getenv("USER_NAME_MYSQL"),
    'password': os.getenv("PASS_MYSQL"),
    'host': os.getenv("MYSQL_HOST"),
    'database': os.getenv("DB_NAME_MYGYM")
}

def connectionToDb():
    return mysql.connector.connect(connectionParameters)


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

def getUser(userID) -> str:
    commandString = 'SELECT user_name FROM dt_main_data_about_users WHERE id= %s'
    data : tuple = (str(userID),)
    cnx = connectionToDb()
    cursor = cnx.cursor(prepared=True)
    cursor.execute(commandString, data)
    result = cursor.fetchone()
    cnx.close()
    if not (result is None) and len(result) > 0:
        return result[0]
    else:
        return ''

def addExerciseToStack(user, exercise, reps = None, minutes = None, weight = None):
    commandS = "INSERT INTO dt_exercises_steck (user, exercise, date, reps, minutes, weight) " \
               "VALUE(%s, %s, %s, %s, %s, %s);"
    data = (user, exercise, datetime.now(), reps, minutes, weight)
    cnx = connectionToDb()
    cursor = cnx.cursor(prepared=True)
    cursor.execute(commandS, data)
    cnx.commit()
    cnx.close()




def addUserToDB():
    commandString = 'Select * From dt_mapping_exercises'
    cnx = connectionToDb()
    cursor = cnx.cursor()
    cursor.execute(commandString)
    result = cursor.fetchall()
    cnx.close()

    pprint.pprint(result)
