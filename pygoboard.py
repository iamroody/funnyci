import socket
import sys
import traceback
import urllib
import webbrowser
from xml.dom import minidom
import time
from cimodel import CiModel
from static import BUILD_VERSION_PATH, jobs, BUILD_STATUS_PATH
from util import util

global build_status
build_status = "off"

def is_build_version_changed(currentBuildVersions):
    oldVersion = util.getDictionaryFromFile(BUILD_VERSION_PATH)
    if not oldVersion.__eq__(currentBuildVersions):
        util.writeDictionaryToFile(currentBuildVersions, BUILD_VERSION_PATH)
        return True
    return False

class Parser(object):
    @staticmethod
    def generate_ci_model_from_xml_string(data):
        dom = minidom.parseString(data)
        activity = {}
        lastBuildStatus = {}
        lastBuildLabel = {}
        lastBuildTime = {}

        for node in dom.getElementsByTagName('Project'):
            stage = node.getAttribute('name')
            for job in jobs:
                if stage == 'home-ideas :: ' + job:
                    activity[job] = node.getAttribute('activity')
                    lastBuildStatus[job] = node.getAttribute('lastBuildStatus')
                    lastBuildLabel[job] = node.getAttribute('lastBuildLabel')
                    lastBuildTime[job] = node.getAttribute('lastBuildTime')

        ciModel = CiModel(activity, lastBuildLabel, lastBuildStatus, lastBuildTime)

        return ciModel

if __name__ == '__main__':
    try:
        socket.setdefaulttimeout(5)

        while True:
            data = open("building-go.xml").read()
    #        data = urllib2.urlopen(urllib2.Request(go_url)).read()

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
                print build_status

            time.sleep(5)

    except Exception, (error):
        traceback.print_exc(file=sys.stdout)
