# -*- coding: utf-8 -*-
import tweepy 
from random import randint
from time import sleep
# First, sign in to Twitter API 

# 各種キーをセット
CONSUMER_KEY = 'psWut2vFh9e1dX0gCV5ICj5rk'
CONSUMER_SECRET = '5MXkpqqEe00Kn5ue1Ie6esBpQa8ocNub7gBCSGXqc4ylNmiMFp'
ACCESS_TOKEN = '718015800133586944-owT6LAObdpEesmHiWbsv80P3acRsmeI'
ACCESS_SECRET = 'sIPWThSDgTB2pp8l3f5d1Na7w7KXkk6sjI4Dww1g0HwFj'

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
