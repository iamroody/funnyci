# -*- coding: utf-8 -*-
import logging
import webbrowser

import web
from datetime import datetime
from config import APP_KEY, APP_SECRET, CALL_BACK_URL
from weibo_oauth2 import APIClient

class Index:
    def GET(self):
        access_token = web.config._session.get('access_token', None)
        expires_in = web.config._session.get('expires_in', None)

        if not access_token:
            logging.info("no session, prepaire go to call back")
            client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
            auth_url = client.get_authorize_url()
            webbrowser.open_new(auth_url)
        else:
            logging.info("find session")
            client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
            client.set_access_token(access_token=access_token, expires_in=expires_in)
            s = u'- %s - 哈哈，可以说中文哦~ this is a post from home ideas ci' % datetime.now().ctime()
            client.post.statuses__update(status=s)


class CallBack:
    def GET(self):
        logging.info("call back")

        i = web.input()
        code = i.get('code', None)
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
        token = client.request_access_token(code)

        web.config._session.access_token = token.access_token
        web.config._session.expires_in = token.expires_in
        logging.info("go to index")

        web.seeother("/")
