import schedule
import tweepy

from data.respository.credentials import twitter
from data.respository.repository import Repository
from domain.trending.trending_topic import TrendingTopic


class TrendingRepository(Repository):
    _SCHEDULE_MINUTES = 10

    def __init__(self, woeid):
        super(TrendingRepository, self).__init__()
        self.api = self._create_api()
        self.woeid = woeid

    def initialize(self):
        self._request_data()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_data)

    @staticmethod
    def _create_api():
        auth = tweepy.OAuthHandler(twitter['api_key'], twitter['api_secret'])
        auth.set_access_token(twitter['access_token'], twitter['access_token_secret'])
        return tweepy.API(auth)

    def _request_data(self):
        result = self.api.trends_place(self.woeid)
        trending_topics = map(lambda json: TrendingTopic(json), result[0]['trends'])
        self.on_data(trending_topics)
