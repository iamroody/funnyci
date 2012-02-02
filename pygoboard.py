import pickle
import socket
import sys
import traceback
import webbrowser
from parser import Parser
from static import jobs


def getOldVersion():
    try:
        f = open('tmp/buildversion', 'r')
        version = pickle.load(f)
        f.close()
        return version
    except EOFError:
        return {}


def writeVersionToFile(currentBuildVersions):
    f = open('tmp/buildversion', 'wb')
    pickle.dump(currentBuildVersions, f)
    f.close()


def is_build_version_changed(currentBuildVersions):
    oldVersion = getOldVersion()
    if not oldVersion.__eq__(currentBuildVersions):
        writeVersionToFile(currentBuildVersions)
        return True
    return False


def getBuildStatus(go_status):
    if all(go_status[job] == 'success' for job in jobs):
        build_status = 'success'
    elif any(go_status[job] == 'building' for job in jobs):
        if any(go_status[job] == 'failure' for job in jobs):
            build_status = 'warning'
        else:
            build_status = 'building'
    elif any(go_status[job] == 'failure' for job in jobs):
        build_status = 'failure'
    else:
        build_status = 'warning'
    return build_status

if __name__ == '__main__':
    try:
        socket.setdefaulttimeout(5)

        document = open("building-go.xml").read()

        parser = Parser()
        ciModel = parser.get_ci_model_from_xml_string(document)
        go_status = ciModel.get_stage_status()
        currentBuildVersions = ciModel.get_build_version()

        if is_build_version_changed(currentBuildVersions):
            build_status = "off"
            print "*** running ***"
            build_status = getBuildStatus(go_status)
            print "weibo will post a weibo with status %s" % build_status
            webbrowser.open_new("http://127.0.0.1:8080/")

    except Exception, (error):
        traceback.print_exc(file=sys.stdout)

