from datetime import datetime
import web
from config import APP_KEY, APP_SECRET, CALL_BACK_URL
from weibo_oauth2 import APIClient

class Weibo:
    def update(self):
        access_token = web.config._session.get('access_token', None)
        expires_in = web.config._session.get('expires_in', None)
        if not access_token:
            print "no session, prepaire go to call back"
            client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
            auth_url = client.get_authorize_url()
            web.redirect(auth_url)
        else:
            print "find session"
            client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
            client.set_access_token(access_token=access_token, expires_in=expires_in)
            s = u'- %s -haha, this is a post from home ideas ci' % datetime.now().ctime()
            client.post.statuses__update(status=s)

