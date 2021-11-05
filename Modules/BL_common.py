import Modules.MySqlHelper as msql
import pprint

from aiogram import types

def parsingMessage(message: types.Message):
    text = message.text
    addExerciseToSteck(text = text, userId = 6666666)
    return 0


def validateExerciseName(exerciseName):
    msql.getNameExcercise(exerciseName)
    return 0

def addExerciseToSteck(text : str, userId):
    arrSplitedText = text.split(".", maxsplit=3)
    if len(arrSplitedText) >= 2:
        msql.addExerciseToStack(user = userId, exercise= arrSplitedText[0].strip(), reps = arrSplitedText[1].strip())
    return 0

def validateUserAccess(userID):
    return msql.getUser(userID)