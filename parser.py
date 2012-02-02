from xml.dom import minidom
from static import jobs

class CiModel:
    def __init__(self, activity, lastBuildLabel, lastBuildStatus, lastBuildTime):
        self.activity = activity
        self.lastBuildLabel = lastBuildLabel
        self.lastBuildStatus = lastBuildStatus
        self.lastBuildTime = lastBuildTime

    def get_stage_status(self):
        stageStatus = {}
        for job in jobs:
            status = self.lastBuildStatus[job].lower() if self.activity[job] != 'Building' else 'building'
            stageStatus[job] = status

        return stageStatus

    def get_build_version(self):
        return self.lastBuildLabel


class Parser(object):
    def get_ci_model_from_xml_string(self, data):
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