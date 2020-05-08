import sys
import time
from datetime import datetime, timedelta, timezone
import tweepy 
from secrets import *


def auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    return api

def post(api):
    fuso = timezone(timedelta(hours=-3))
    while (api.verify_credentials):
        api.update_status('{}!\nLave as mãos, beba água e mantenha a higiene.\n#FicaEmCasa CUIDE DE QUEM VOCÊ AMA!\n#homeoffice #coronavirus #pandemia #covid19 #quarentena #FiqueEmCasa'.format(datetime.now().astimezone(fuso).strftime('%d/%m/%Y %H:%M')))
        time.sleep(5400)

if( __name__ == "__main__"):

    auth_true = auth()
    post(auth_true)

sys.exit()