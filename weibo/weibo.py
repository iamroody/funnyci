from datetime import datetime
from config import ACCESS_TOKEN_SECRET, ACCESS_TOKEN, APP_KEY, APP_SECRET
from data import Weibo_Message, GEOGRAPHY
from weibo_oauth1 import OAuthToken, APIClient

class WeiBo:
    @staticmethod
    def postWeiboUpdate(build_status):
        access_token = OAuthToken(oauth_token=ACCESS_TOKEN, oauth_token_secret=ACCESS_TOKEN_SECRET)
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, token=access_token)
        content = u'%s - %s' % (Weibo_Message[build_status], datetime.now().ctime())
        client.post.statuses__update(status=content, lat=GEOGRAPHY['lat'], long=GEOGRAPHY['long'])
