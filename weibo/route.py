import web
from config import APP_KEY, APP_SECRET, CALL_BACK_URL
from weibo_oauth2 import APIClient

class Index:
    def GET(self):
        access_token = web.config._session.get('access_token', None)
        if not access_token:
            client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
            auth_url = client.get_authorize_url()
            web.seeother(auth_url)


class CallBack:
    def GET(self):
        i = web.input()
        code = i.get('code', None)
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALL_BACK_URL)
        token = client.request_access_token(code)

        access_token = token.access_token
        expires_in = token.expires_in

        client.set_access_token(access_token=access_token, expires_in=expires_in)

        client.post.statuses__update("this is a song from broken CI")



