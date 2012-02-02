import pickle
import socket
import sys
import traceback
from parser import Parser
from static import jobs

if __name__ == '__main__':
    try:
        socket.setdefaulttimeout(5)

        document = open("building-go.xml").read()

        parser = Parser()

        go_status = parser.get_ci_model_from_xml_string(document).get_stage_status()
        currentBuildVersions = parser.get_ci_model_from_xml_string(document).get_build_version()

        f = open('tmp/buildversion', 'wb')
        pickle.dump(currentBuildVersions, f)
        f.close()

        f = open('tmp/buildversion', 'r')
        test = pickle.load(f)
        f.close()

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
