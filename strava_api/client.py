from pystrava import Strava
import os


class Client:
    def __init__(self):
        self.strava = Strava(client_id=os.environ['CLIENT_ID'],
                             client_secret=os.environ['SECRET'],
                             callback=os.environ['CALLBACK_URL'],
                             scope=os.environ['SCOPE'],
                             email=os.environ['EMAIL'],
                             password=os.environ['PASSWORD'])
        self.activities = self.strava.get_activities(limit=500)
