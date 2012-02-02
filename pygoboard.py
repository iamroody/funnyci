import socket
import sys
import traceback
import webbrowser
from parser import Parser
from static import BUILD_VERSION_PATH
from util import util

def is_build_version_changed(currentBuildVersions):
    oldVersion = util.getDictionaryFromFile(BUILD_VERSION_PATH)
    if not oldVersion.__eq__(currentBuildVersions):
        util.writeDictionaryToFile(currentBuildVersions, BUILD_VERSION_PATH)
        return True
    return False


if __name__ == '__main__':
    try:
        socket.setdefaulttimeout(5)

        data = open("building-go.xml").read()

        ciModel = Parser.generate_ci_model_from_xml_string(data)
        go_status = ciModel.get_stage_status()
        currentBuildVersions = ciModel.get_build_version()

        print "*** running ***"

        if is_build_version_changed(currentBuildVersions):
            build_status = ciModel.getBuildStatus(go_status)
            print "weibo will post a weibo with status %s" % build_status
            webbrowser.open_new("http://127.0.0.1:8080/")
        else:
            print "*** not changed ***"

    except Exception, (error):
        traceback.print_exc(file=sys.stdout)

