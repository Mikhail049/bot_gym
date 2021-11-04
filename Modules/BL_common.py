import Modules.MySqlHelper as msql

from aiogram import types

async def parsingMessage(message: types.Message):
    text = message.text
    userId = message.from_user
    validateExerciseName(text)
    return 0


async def validateExerciseName(exerciseName):
    msql.getNameExcercise(exerciseName)
    return 0

async def addExerciseToSteck():

    return 0

async def validateUserAccess(UserID):
    return 0