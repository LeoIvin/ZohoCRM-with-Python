from zcrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature
from zcrmsdk.src.com.zoho.crm.api import Initializer
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
grant_token = os.getenv('GRANT_TOKEN')
redirect_url = os.getenv('REDIRECT_URL')

user = UserSignature("use user email")

root_dir = os.path.dirname(os.path.abspath(__file__))
logger_file_path = os.path.join(root_dir, 'logfile.log')


class SDKInitializer:

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()

        token = OAuthToken(client_id=client_id, client_secret=client_secret, grant_token=grant_token,
                           redirect_url=redirect_url)

        logger = Logger.get_instance(level=Logger.Levels.INFO, file_path=logger_file_path)

        Initializer.initialize(user=user, environment=environment, token=token, logger=logger)


# Call to initialize the SDK
SDKInitializer.initialize()
