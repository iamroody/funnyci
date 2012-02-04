import random
import socket
import subprocess
import sys
import threading
import traceback
import urllib2
import time
from parser import Parser
from service import is_build_version_changed, getRandomTestXML
from static import BUILD_STATUS_PATH, Say_Message, Twitter_Message
from twitter.t import Twitter
from util import util

def threadWeiBo():
    urllib2.urlopen("http://127.0.0.1:8080/")


def threadSay(build_status):
    command = "say %s" % Say_Message[build_status]
    subprocess.call(command, shell=True)


def threadTwitter(build_status):
    status = Twitter_Message[build_status]
    Twitter.postTwitterUpdate(status)


def createTaskThreads(build_status):
    say = threading.Thread(target=threadSay, args=(build_status,))
    say.start()
    weibo = threading.Thread(target=threadWeiBo)
    weibo.start()
    twitter = threading.Thread(target=threadTwitter)
    twitter.start()


if __name__ == '__main__':
    try:
        socket.setdefaulttimeout(5)

        while True:
            build_status = "off"
            data = open(getRandomTestXML()).read()
            #            data = urllib2.urlopen(urllib2.Request('http://go.hi-ci.vpc.realestate.com.au:8153/go/cctray.xml')).read()

            ciModel = Parser.generate_ci_model_from_xml_string(data)
            go_status = ciModel.get_stage_status()
            currentBuildVersions = ciModel.get_build_version()

            print "*** running ***"

            if is_build_version_changed(currentBuildVersions):
                build_status = ciModel.getBuildStatus(go_status)
                print "weibo will post a weibo with status %s" % build_status
                util.writeToFile(BUILD_STATUS_PATH, build_status)
                createTaskThreads(build_status)

            else:
                print "*** not changed ***"
                print build_status

            time.sleep(5)

    except Exception, (error):
        traceback.print_exc(file=sys.stdout)
