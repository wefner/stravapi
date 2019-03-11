from pystrava import Strava
import os


class Client:
    """
    Strava object to wrap authentication and activities.

    """
    def __init__(self, limit=500):
        """
        Initialise object
        """
        self._strava = None
        self.limit = limit

    @property
    def strava(self):
        """
        Client authenticated.

        Caching the object so we don't call it every time.
        :return:
        """
        if not self._strava:
            self._strava = Strava(client_id=os.environ['CLIENT_ID'],
                                  client_secret=os.environ['SECRET'],
                                  callback=os.environ['CALLBACK_URL'],
                                  scope=os.environ['SCOPE'],
                                  email=os.environ['EMAIL'],
                                  password=os.environ['PASSWORD'])
        return self._strava

    @property
    def activities(self):
        """
        Gets all activities for a given user.

        Limit is set when initializing and cannot be overwritten here.
        :return: list of Activity objects
        """
        return self.strava.get_activities(limit=self.limit)
