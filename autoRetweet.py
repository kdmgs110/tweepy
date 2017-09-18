# -*- coding: utf-8 -*-
import tweepy 
from random import randint
from time import sleep
# First, sign in to Twitter API 

# 各種キーをセット
CONSUMER_KEY = '5WiNRDJX83huEYYwvL29akUCr'
CONSUMER_SECRET = 'BEpxsOpXqBuzchPNsnWaoPKhJQ87k3W7wc1d4E7jAwanvnplVD'
ACCESS_TOKEN = '909614734743179265-Cx2PkIiwizhP9I0mDJeJ7XGj43iTVEb'
ACCESS_SECRET = 'CTXx3tnCwTPDhKh2HwCY2N1AIi9DMVIQdrcSBZVWArP14'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成

api = tweepy.API(auth)

q = "the-academic-times.com"  #検索するURL
count = 50 # 検索数
yourAccount = "never_be_a_pm"

try:
    searchResults = api.search(q=q, count=count) #検索
    for result in searchResults:
        screenId = result.user._json['screen_name']
        userId = result.id
        print("##############################")
        print('検索したユーザーのID:{}'.format(screenId))
        print("ツイート:{}".format(result.text))
        print("作成日時:{}".format(result.created_at))
        if(yourAccount == screenId):
            print("・自分自身ですので、スキップします")
            continue
        else:
            try:
                api.create_favorite(userId)
                print("・お気に入りしました")
            except Exception as e:
                print("・すでにお気に入りしています")
                print(e)
            try:
                api.retweet(userId) #フォローする
                print("リツイートしました")
                sleep(randint(10,20))
            except Exception as e:
                print("ID{}はすでにリツイートしています".format(userId))
                print(e)
                continue;  
except Exception as e:
    print(e)
