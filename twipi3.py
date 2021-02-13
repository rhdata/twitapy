import tweepy
from tweepy.auth import OAuthHandler
from unidecode import unidecode



consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

filename = ""


fmt = '%Y-%m-%d %H:%M:%S'

# BOUCLE ICI ???
list_id = list()
list_tweets = list()
list_times = list()
list_screen_name = list()
for j in range(0,4) : 
    print ("###### REQUETE N° ", j)

   
    if len(list_id) != 0 :
        res =  api.search("",lang = "",count = 300, result_type = "recent", max_id = min(list_id))
    else : # Sinon
        res = api.search("",lang = "",count = 300, result_type = "recent")
    
    # On stocke les tweets et on les printe
    for i in range(len(res)):

        print(i, res[i].text)
        list_tweets.append(res[i].text)
        list_id.append(res[i].id)
        list_times.append(res[i].created_at.strftime(fmt))
        list_screen_name.append(res[i].user.screen_name)
            
