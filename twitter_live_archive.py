import os
import time 
import csv
import json
import pandas as pd 
import tweepy
import waybackpy

auth = tweepy.OAuthHandler(os.environ.get('twitter_consumer_key'), os.environ.get('twitter_consumer_secret'))
auth.set_access_token(os.environ.get('twitter_access_key'), os.environ.get('twitter_access_secret'))
api = tweepy.API(auth)

user = 'michaeljburry'

if not os.path.exists('store'):
    os.makedirs('store')

open("id.txt", "w")

def retrieve():
	f = open('id.txt', 'r')
	nums = f.readlines()
	ids = [int(i) for i in nums]
	f.close()
	return ids

def archive(id):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    url = 'https://twitter.com/' + user + '/status/' + str(id)
    wayback = waybackpy.Url(url, user_agent)
    archive = wayback.save()
    print(archive.archive_url)
    return

def store(id, tweet):
    f_write = open('id.txt', 'w')
    f_write.write(str(id))
    f_write.close()
    with open('./store/'+str(id)+'.json', 'w') as outfile:
        json.dump(tweet[0]._json, outfile)
    return

def run(i):
    print('retrieving...', flush=True)
    ids = retrieve()
    tweet = api.user_timeline(screen_name=user, count=1, include_rts = False)
    if ((len(tweet)>0) and (tweet[0].id not in ids)):
        print('saving...', flush=True)
        store(tweet[0].id, tweet)
        print('submitting to archive...', flush=True)
        archive(tweet[0].id)
        i = i+1
    else:
    	i = i
    return(i)

i = 0

while True:
    i = run(i)
    time.sleep(3)

