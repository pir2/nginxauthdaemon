import requests
from auth import Authenticator


class PIAuthenticator(Authenticator):
    """privacyidea authenticator. Requires configuration options PI_URL"""
    def __init__(self, config):
        super(PIAuthenticator, self).__init__(config)

        self._app_url = config['PI_URL']

    def authenticate(self, username, password):
        if username == None or password == None or len(username)==0 or len(password)==0:
            return False

        url = self._app_url + "/validate/check"
        r = requests.post(url=url,
                          data={"user":username
                               ,"pass":password
                               }
                          )

        result = r.json()

        if result == None:
            # auth failed
            return False
        # auth succeeded
        return result["result"]["value"]
