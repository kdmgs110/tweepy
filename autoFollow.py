# -*- coding: utf-8 -*-
import tweepy 
"""

Procedure
* Sign in Twitter Account
* Make list object that contains tweet refering to certain url 
* Randomly select one tweet content, and tweet
* get userid
    + if you've alreadly follow him, just like him.
    + if not, like him and follow him, retweet his post.
* wait for certain seconds in order to act human-like
* do same action again till arraylist's size equals to zero 

* If you are new to tweepy, see http://tweepy.readthedocs.io/en/v3.5.0/
"""

# 各種キーをセット
CONSUMER_KEY = 'psWut2vFh9e1dX0gCV5ICj5rk'
CONSUMER_SECRET = '5MXkpqqEe00Kn5ue1Ie6esBpQa8ocNub7gBCSGXqc4ylNmiMFp'
ACCESS_TOKEN = '718015800133586944-owT6LAObdpEesmHiWbsv80P3acRsmeI'
ACCESS_SECRET = 'sIPWThSDgTB2pp8l3f5d1Na7w7KXkk6sjI4Dww1g0HwFj'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成

api = tweepy.API(auth)

# 検索するurlを指定

q = "the-academic-times.com"  #検索するURL
count = 50 # 検索数
yourAccount = "never_be_a_pm"

try:
    searchResults = api.search(q=q, count=count) #検索
    print("{}としてログインしました".format(api.me))
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
        try:
            api.create_favorite(userId)
            print("・お気に入りしました")
            #TODO add favrite method
        except Exception as e:
            print("・すでにお気に入りしています")
            print(e)
            continue
        try:
            api.create_friendship(screenId) #フォローする
            print("・フォローしました")
        except:
            print("ID{}はすでにフォローしています。次の処理を開始します".format(screenId))
            continue;       
except Exception as e:
    print(e)   
