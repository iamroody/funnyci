# -*- coding: utf-8 -*-
import webbrowser
import sys
import os
import web

PROJECT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_DIR, '../'))

from config import APP_KEY, APP_SECRET, CALL_BACK_URL
from weibo_oauth1 import APIClient

class Index:
    def GET(self):
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, callback=CALL_BACK_URL)
        request_token = client.get_request_token()
        web.config._session.request_token = request_token
        auth_url = client.get_authorize_url(request_token.oauth_token)
        webbrowser.open_new(auth_url)

        return u"redirect to auth url"


class CallBack:
    def GET(self):
        i = web.input()
        verifier = i.get('oauth_verifier', None)
        request_token = web.config._session.get('request_token', None)
        request_token.oauth_verifier = verifier

        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, token=request_token)
        access_token = client.get_access_token()


