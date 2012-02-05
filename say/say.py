import subprocess
from data import Say_Message

class Say:
    @staticmethod
    def sayThis(build_status):
        command = "say %s" % Say_Message[build_status]
        subprocess.call(command, shell=True)
