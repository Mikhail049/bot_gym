import Modules.MySqlHelper as msql
import pprint

from aiogram import types

def parsingMessage(message: types.Message):
    pprint.pprint("Start parsingMessage")
    text = message.text
    userId = message.from_user.id
    pprint.pprint(userId)
    addExerciseToSteck(text = text, userId = userId)
    return 0


def validateExerciseName(exerciseName):
    msql.getNameExcercise(exerciseName)
    return 0

def addExerciseToSteck(text : str, userId):
    pprint.pprint("Start addExerciseToSteck")
    arrSplitedText = text.split(".")
    pprint.pprint(arrSplitedText)
    if len(arrSplitedText) >= 1:
        msql.addExerciseToStack(user = userId, exercise= str(arrSplitedText[0]), reps = str(arrSplitedText[1]))
    return 0

def validateUserAccess(userID):
    return msql.getUser(userID)