import urllib2, socket, random
import json, datetime, os, sys
import traceback
from xml.dom import minidom

jobs = ['package', 'acceptance_standalone', 'acceptance_staging']
go_url = 'http://go.hi-ci.vpc.realestate.com.au:8153/go/cctray.xml'

def get_status_from_xml():
    document = urllib2.urlopen(urllib2.Request(go_url)).read()

    dom = minidom.parseString(document)
    stageStatus = {}

    for node in dom.getElementsByTagName('Project'):
        stage = node.getAttribute('name')
        for job in jobs:
            if stage == 'home-ideas :: ' + job:
                activity = node.getAttribute('activity')
                last_build_status = node.getAttribute('lastBuildStatus')
                stageStatus[job] = get_stage_status(activity, last_build_status)
    return stageStatus


def get_stage_status(activity, last_build):
    if activity == 'Building':
        return 'building'
    return last_build.lower()

if __name__ == '__main__':
    try:
        socket.setdefaulttimeout(5)

        go_status = get_status_from_xml()

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

        print "currnet status:" + build_status

    except Exception, (error):
        traceback.print_exc(file=sys.stdout)
