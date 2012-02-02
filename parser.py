from xml.dom import minidom
from cimodel import CiModel
from static import jobs


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