import random
import socket
import subprocess
import sys
import threading
import traceback
import time
import urllib2
from parser import Parser
from static import Say_Message, REAL_GO, TEST_FILES
from twitter.twitter import Twitter
from weibo.weibo import WeiBo

def threadWeiBo(build_status):
    WeiBo.postWeiboUpdate(build_status)


def threadSay(build_status):
    command = "say %s" % Say_Message[build_status]
    subprocess.call(command, shell=True)


def threadTwitter(build_status):
    Twitter.postTwitterUpdate(build_status)


def createTaskThreads(build_status):
    say = threading.Thread(target=threadSay, args=(build_status,))
    say.start()
    weibo = threading.Thread(target=threadWeiBo, args=(build_status,))
    weibo.start()
    twitter = threading.Thread(target=threadTwitter, args=(build_status,))
    twitter.start()


def readTestData():
    file_path = "test-data/%s" % random.choice(TEST_FILES)
    return open(file_path).read()


def readRealData():
    return urllib2.urlopen(REAL_GO).read()


if __name__ == '__main__':
    try:
        socket.setdefaulttimeout(5)
        oldBuildVersions = {}
        build_status = "off"

        while True:
            data = readTestData()

            ciModel = Parser.generate_ci_model_from_xml_string(data)
            go_status = ciModel.get_stage_status()
            currentBuildVersions = ciModel.get_build_version()

            print "*** running ***"

            if not currentBuildVersions.__eq__(oldBuildVersions):
                print "*** it seems that there is a new build ***"
                build_status = ciModel.getBuildStatus(go_status)
                print "*** it seems that current build status is %s" % build_status
                createTaskThreads(build_status)
                oldBuildVersions = currentBuildVersions
            else:
                print "*** it seems that nothing happen ***"

            time.sleep(5)

    except Exception, (error):
        traceback.print_exc(file=sys.stdout)
