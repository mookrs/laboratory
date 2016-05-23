from secrets import *
from twitter import *
import os

MY_TWITTER_CREDS = "my_app_credentials"
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance(MY_APP_NAME, CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=5)
print(pythonStatuses)
