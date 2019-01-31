from utilities import * 
import os
import PySimpleGUIQt as p
import screens

# CONSTANTS

CURRENT_DIRECTORY = os.path.realpath(os.path.dirname(__file__))
DOWNLOAD_DIRECTORY = getRealPath(CURRENT_DIRECTORY + "/download/")

if checkFutureRestore() == False: 
    screens.futureRestoreQuestion()
elif checkFutureRestore() == True:
    pass
screens.mainScreen()


