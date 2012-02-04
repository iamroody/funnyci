import random
from static import BUILD_VERSION_PATH
from util import util

def is_build_version_changed(currentBuildVersions):
    oldVersion = util.getDictionaryFromFile(BUILD_VERSION_PATH)
    if not oldVersion.__eq__(currentBuildVersions):
        util.writeDictionaryToFile(currentBuildVersions, BUILD_VERSION_PATH)
        return True
    return False


def getRandomTestXML():
    file_name = ['building-go.xml', 'failed-go.xml', 'successful-go.xml', 'warning-go.xml']
    return "test-data/%s" % random.choice(file_name)