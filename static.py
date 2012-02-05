# -*- coding: utf-8 -*-

JOBS = ['package', 'acceptance_standalone', 'acceptance_staging']
TEST_FILES = ['building-go.xml', 'failed-go.xml', 'successful-go.xml', 'warning-go.xml']
REAL_GO = 'http://go.hi-ci.vpc.realestate.com.au:8153/go/cctray.xml'

Weibo_Message = {
    "building": u"一次新的build开始了！有木有? 好运哦！ 亲！",
    "warning": u"有人在修Build，这次一定要绿哦！",
    "success": u"撒花啊！过了，有木有！可以回家了，有木有！下一对提交的要抢token了！",
    "failure": u"讨厌你！讨厌你！都是你的错！赶快过来修build"
}

Say_Message = {
    "building": u"Good luck ! Baby !",
    "warning": u"Some One is fixing build now ! Good luck !",
    "success": u"oh yeah! Build is green now ! Attention please !",
    "failure": u"Warning ! Warning ! Build is broken !"
}

Twitter_Message = {
    "building": u"Good luck ! Baby !",
    "warning": u"Some One is fixing build now ! Good luck !",
    "success": u"oh yeah! Build is green now ! Attention please !",
    "failure": u"Warning ! Warning ! Build is broken !"
}
