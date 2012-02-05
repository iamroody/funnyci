from static import JOBS

class CiModel:
    def __init__(self, activity, lastBuildLabel, lastBuildStatus, lastBuildTime):
        self.activity = activity
        self.lastBuildLabel = lastBuildLabel
        self.lastBuildStatus = lastBuildStatus
        self.lastBuildTime = lastBuildTime

    def get_stage_status(self):
        stageStatus = {}
        for job in JOBS:
            status = self.lastBuildStatus[job].lower() if self.activity[job] != 'Building' else 'building'
            stageStatus[job] = status

        return stageStatus

    def getBuildStatus(self, go_status):
        if all(go_status[job] == 'success' for job in JOBS):
            build_status = 'success'
        elif any(go_status[job] == 'building' for job in JOBS):
            if any(go_status[job] == 'failure' for job in JOBS):
                build_status = 'warning'
            else:
                build_status = 'building'
        elif any(go_status[job] == 'failure' for job in JOBS):
            build_status = 'failure'
        else:
            build_status = 'warning'

        return build_status


    def get_build_version(self):
        return self.lastBuildLabel
