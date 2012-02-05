from datetime import datetime
import twitter_api
from static import Twitter_Message
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

class Twitter:
    @staticmethod
    def postTwitterUpdate(build_status):
        api = twitter_api.Api(consumer_key=CONSUMER_KEY,
                              consumer_secret=CONSUMER_SECRET,
                              access_token_key=ACCESS_TOKEN_KEY,
                              access_token_secret=ACCESS_TOKEN_SECRET,
                              debugHTTP=True)
        content = u'- %s - %s' % (datetime.now().ctime(), Twitter_Message[build_status])

        api.PostUpdate(content)


