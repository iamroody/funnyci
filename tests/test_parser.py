# -*- coding: utf-8 -*-

from datetime import datetime
import unittest
from parser import Parser

def createTestData(activity, lastBuildStatus):
    xml_template = """<?xml version="1.0" encoding="utf-8"?>
              <Projects>
              <Project name="home-ideas :: package" activity="%s" lastBuildStatus="%s" lastBuildLabel="480 :: 3" lastBuildTime="2012-02-01T21:47:52" webUrl="http://go/pipelines/home-ideas/480/package/3" />
              <Project name="home-ideas :: acceptance_standalone" activity="%s" lastBuildStatus="%s" lastBuildLabel="480 :: 3" lastBuildTime="2012-02-01T21:47:52" webUrl="http://go/pipelines/home-ideas/480/package/3" />
              <Project name="home-ideas :: acceptance_staging" activity="%s" lastBuildStatus="%s" lastBuildLabel="480 :: 3" lastBuildTime="2012-02-01T21:47:52" webUrl="http://go/pipelines/home-ideas/480/package/3" />
              </Projects>"""

    return xml_template % (activity, lastBuildStatus, activity, lastBuildStatus, activity, lastBuildStatus)


class testParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_get_ci_model_from_xml_string(self):
        data = createTestData(activity="Sleeping", lastBuildStatus="Success")
        ciModel = self.parser.generate_ci_model_from_xml_string(data)
        self.assertEqual(ciModel.activity['package'], "Sleeping")
        self.assertEqual(ciModel.lastBuildStatus['acceptance_standalone'], "Success")
        status = ciModel.get_stage_status()
        self.assertEqual(status['package'], "success")

    def test_date(self):
        print u'- %s - haha, this is a 中文t from home' % datetime.now().ctime()
