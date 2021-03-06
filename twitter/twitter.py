import twitter_api
from datetime import datetime
from data import Twitter_Message
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

class Twitter:
    @staticmethod
    def postTwitterUpdate(build_status):
        api = twitter_api.Api(consumer_key=CONSUMER_KEY,
                              consumer_secret=CONSUMER_SECRET,
                              access_token_key=ACCESS_TOKEN_KEY,
                              access_token_secret=ACCESS_TOKEN_SECRET,
                              debugHTTP=True)
        content = u'- %s - %s' % (Twitter_Message[build_status], datetime.now().ctime())

        api.PostUpdate(content)


