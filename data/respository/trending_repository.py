import schedule
import tweepy

from data.respository.credentials import twitter
from data.respository.repository import Repository
from domain.trending.trending_topic import TrendingTopic


class TrendingRepository(Repository):
    """
    The Twitter credentials are stored in credentials.py
    The file is excluded from the git repository
    The app credentials can be found here: https://developer.twitter.com/en/apps/
    """
    _SCHEDULE_MINUTES = 10

    def __init__(self, woeid):
        super(TrendingRepository, self).__init__()
        self.api = self._create_api()
        self.woeid = woeid

    @staticmethod
    def _create_api():
        auth = tweepy.OAuthHandler(twitter['api_key'], twitter['api_secret'])
        auth.set_access_token(twitter['access_token'], twitter['access_token_secret'])
        return tweepy.API(auth)

    def initialize(self):
        self._request_data()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_data)

    def _request_data(self):
        result = self.api.trends_place(self.woeid)
        trending_topics = []
        for json in result[0]['trends']:
            trending_topics.append(TrendingTopic(json))
        self.on_data(trending_topics)
