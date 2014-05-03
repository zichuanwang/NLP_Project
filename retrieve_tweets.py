# -*- coding:utf-8 -*- 
# Author: Zichuan Wang
# Last Update: 5/1/2014

import sys, tweepy

consumer_key="STWE4HcDWypqIrhRQiFuW2EdJ"
consumer_secret="3UpxUuyWvEmc9A2Pya6raWJEFFNq2JDpBXaPUusoa9FgSTE11B"

access_token="514188693-X8W6lPFPUgJyTXjwlUgcGhAyCifCgNudBg1FZIVx"
access_token_secret="POp9CbNvozE8rGTVeYmFgB6OoJkKeAHAN2Za5lsP6m1XF"

def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

def check_input_validity(cmds):
    if len(cmds) != 1:
        return False
    return True

if __name__ == "__main__":
    if check_input_validity(sys.argv[1:]):
        api = get_api()
        tweets = api.user_timeline(sys.argv[1])
        for tweet in tweets:
            print tweet.text
    else:
        print "Usage: python retrieve_tweets.py id/user_id/screen_name"