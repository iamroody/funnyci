# -*- coding: utf-8 -*-
import logging
import webbrowser
import sys
import os
import web

PROJECT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_DIR, '../'))

from datetime import datetime
from config import APP_KEY, APP_SECRET, CALL_BACK_URL
from weibo_oauth2 import APIClient
from static import BUILD_STATUS_PATH, Weibo_Message
from util import util

class Index:
    def GET(self):
        access_token = web.config._session.get('access_token', None)
        expires_in = web.config._session.get('expires_in', None)
        content = ""

        if not access_token:
            print("no session, prepaire go to call back")
            client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
            auth_url = client.get_authorize_url()
            webbrowser.open_new(auth_url)
        else:
            print("find session")
            client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
            client.set_access_token(access_token=access_token, expires_in=expires_in)
            build_status = util.readFromFile(BUILD_STATUS_PATH)
            content = u'- %s - %s' % (datetime.now().ctime(), Weibo_Message[build_status])
            client.post.statuses__update(status=content)

        return u"success-%s" % content


class CallBack:
    def GET(self):
        print("call back")

        i = web.input()
        code = i.get('code', None)
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
        token = client.request_access_token(code)

        web.config._session.access_token = token.access_token
        web.config._session.expires_in = token.expires_in
        print("go to index")

        web.seeother("/")
