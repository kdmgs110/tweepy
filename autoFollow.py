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
CONSUMER_KEY = '5WiNRDJX83huEYYwvL29akUCr'
CONSUMER_SECRET = 'BEpxsOpXqBuzchPNsnWaoPKhJQ87k3W7wc1d4E7jAwanvnplVD'
ACCESS_TOKEN = '909614734743179265-Cx2PkIiwizhP9I0mDJeJ7XGj43iTVEb'
ACCESS_SECRET = 'CTXx3tnCwTPDhKh2HwCY2N1AIi9DMVIQdrcSBZVWArP14'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成

api = tweepy.API(auth)

# 検索するurlを指定

q = "the-academic-times.com"  #検索するURL
count = 50 # 検索数
yourAccount = "never_be_a_pm"
followCount = 0

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
            followCount = followCount + 1
        except:
            print("ID{}はすでにフォローしています。次の処理を開始します".format(screenId))
            continue;       
    print("合計{}人フォローしました".format(followCount))
except Exception as e:
    print(e)   
