import Modules.MySqlHelper as msql

def parsingMessage(message):
    validateExerciseName(message)
    return 0


def validateExerciseName(exerciseName):
    msql.getNameExcercise(exerciseName)
    return 0