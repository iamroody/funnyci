import urllib2, socket, random
import json, datetime, os, sys
import traceback
from xml.dom import minidom
from parser import Parser
from static import jobs

go_url = 'http://go.hi-ci.vpc.realestate.com.au:8153/go/cctray.xml'
oldBuildVersions = {}

def get_status_from_xml():
#    document = urllib2.urlopen(urllib2.Request(go_url)).read()
    document = open("building-go.xml").read()
    dom = minidom.parseString(document)
    stageStatus = {}
    buildVersions = {}

    for node in dom.getElementsByTagName('Project'):
        stage = node.getAttribute('name')
        for job in jobs:
            if stage == 'home-ideas :: ' + job:
                activity = node.getAttribute('activity')
                last_build_status = node.getAttribute('lastBuildStatus')
                buildVersions[job] = node.getAttribute('lastBuildLabel')
                stageStatus[job] = get_stage_status(activity, last_build_status)
    return stageStatus,buildVersions

def is_build_version_changed(newBuildVersions, oldBuildVersions):
    return not newBuildVersions.__eq__(oldBuildVersions)

def get_stage_status(activity, last_build):
    if activity == 'Building':
        return 'building'
    return last_build.lower()

if __name__ == '__main__':
    try:
        socket.setdefaulttimeout(5)

        document = open("building-go.xml").read()

        parser = Parser()

        go_status = parser.get_ci_model_from_xml_string(document).get_stage_status()
        currentBuildVersions = parser.get_ci_model_from_xml_string(document).lastBuildLabel

        oldBuildVersions = currentBuildVersions

        build_status = "off"

        print "*** running ***"

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

        print build_status
    except Exception, (error):
        traceback.print_exc(file=sys.stdout)
