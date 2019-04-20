import os
import sys
import requests
import zipfile

CURRENT_DIRECTORY = os.path.realpath(os.path.dirname(__file__))

platform = sys.platform

def getRealPath(path):
    real_path = os.path.realpath(path)
    return real_path
DOWNLOAD_DIRECTORY = getRealPath(CURRENT_DIRECTORY + "/download/")

def getFutureRestore():
    if platform == "linux" or platform == "linux1" or platform == "linux2":
        git_link = "https://github.com/s0uthwest/futurerestore/releases/download/191/futurerestore_linux_v191.zip"
    elif platform == "darwin":
        git_link = "https://github.com/s0uthwest/futurerestore/releases/download/231/futurerestore_v231_macOS.zip"
    elif platform == "win32" or platform == "win64":
        git_link = "https://github.com/s0uthwest/futurerestore/releases/download/231/futurerestore_v231_win64.zip"
    else:
        git_link = ""
    return git_link

def downloadFutureRestore():
    git_link = getFutureRestore()
    r = requests.get(git_link, allow_redirects=True)
    if platform == "win32" or platform == "win64":
        name = "/futurerestore.exe"
    elif platform == "linux" or platform == "linux1" or platform == "linux2" or platform == "darwin":
        name = "/futurerestore"
    open(DOWNLOAD_DIRECTORY + "/futurerestore.zip", 'wb').write(r.content)
    zip_ref = zipfile.ZipFile(DOWNLOAD_DIRECTORY + "/futurerestore.zip", 'r')
    zip_ref.extractall(DOWNLOAD_DIRECTORY)
    zip_ref.close()
    if platform == 'linux' or platform == "linux1" or platform == "linux2" or platform == "darwin":
        os.chmod(DOWNLOAD_DIRECTORY + '/futurerestore', 775)
def checkFutureRestore():
    if platform == "win32" or platform == "win64":
        if os.path.exists(getRealPath(DOWNLOAD_DIRECTORY + "/futurerestore.exe")):
            return True
        else:
            return False
    elif platform == "linux" or platform == "linux1" or platform == "linux2" or platform == "darwin":
        if os.path.exists(getRealPath(DOWNLOAD_DIRECTORY + "/futurerestore")):
            return True
        else:
            return False
    else:
        return False

def getTypeFutureRestore():
    if platform == 'linux' or platform == 'linux1' or platform == 'linux2' or platform == 'darwin':
        return 1
    elif platform == 'win32' or platform == 'win64':
        return 2

    

