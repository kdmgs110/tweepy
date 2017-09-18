# -*- coding: utf-8 -*-
import tweepy 

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

userid = "never_be_a_pm"

followers_id = api.followers_ids(userid) #自分のアカウントのフォロワーをすべて取得する
following_id = api.friends_ids(userid) #自分のアカウントのフォロイングをすべて取得する
for following in following_id: #自分がフォローしているユーザーだけ取得する
    if following not in followers_id: #自分のフォローしているユーザーで、フォロワーに属さなユーザーを取得する　
        userfollowers = api.get_user(following).followers_count
        if userfollowers < 100:
            print("リムーブするユーザー名:{}".format(api.get_user(following).name))
            print("フォロワー数:".format(userfollowers))
            api.destroy_friendship(following)