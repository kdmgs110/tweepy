# -*- coding: utf-8 -*-
import tweepy 

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

userid = "never_be_a_pm"
count = 0

followers_id = api.followers_ids(userid) #自分のアカウントのフォロワーをすべて取得する
following_id = api.friends_ids(userid) #自分のアカウントのフォロイングをすべて取得する
for following in following_id: #自分がフォローしているユーザーだけ取得する
    if following not in followers_id: #自分のフォローしているユーザーで、フォロワーに属さなユーザーを取得する　
        userfollowers = api.get_user(following).followers_count
        if userfollowers < 100:
            try:
                print("リムーブするユーザー名:{}".format(api.get_user(following).name))
                print("フォロワー数:{}".format(userfollowers))
                api.destroy_friendship(following)
                print("リムーブしました")
                count = count + 1
                print("{}人リムーブしました".format(count))
                break
            except Exception as e:
                print(e)
            