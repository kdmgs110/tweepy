# -*- coding: utf-8 -*-
import tweepy 
import random # ランダムでツイートを選ぶときに使う
"""
Procedure
* Sign in Twitter Accout
* Make list object that contains tweet content
* Randomly select one tweet content, and tweet
* automate tweeting 
"""
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

#ツイートをリストに格納

tweets = [
      #''' 1'''  
              "「機械で替えがきく教師は替えるべきだ」。そして「子どもたちが興味を抱いたとき、そこに教育が生まれる」。 現場でそれを目にするたびに 彼のことを思い出します。" #1 
              + "{}".format("http://www.the-academic-times.com/2017/05/self-organized-learning-environment.html"),

      #''' 2'''  
              "その結果、驚くべきことが判明しました。母親の教育によって、子どもの遺伝子が再構築されていたのです。" #2
              + "{}".format("http://www.the-academic-times.com/2017/05/education-can-change-genes.html"),
        
      #''' 3'''  
              "こうした様々な状況において 、ある一つの特徴が大きく成功を左右していました。それは 社会的知性ではありません 。ルックスでも、 身体的健康でも、 IQでもありませんでした。" #3
              + "{}".format("http://www.the-academic-times.com/2017/07/grit.html"),
              
      #''' 4'''  
              "次に私は小論文を書くことを教えようとしました。でもそれはまず不可能だとわかりました。学生たちは単に押し付けられた考え方に従うだけだったのです。 " #4
              + "{}".format("http://www.the-academic-times.com/2017/09/teaching-in-north-korea.html"),
              
      #''' 5'''  
              "大学時代、教科書が非常に高かった記憶はありませんか。今回はそんな高すぎる教科書業界に、風穴を開けるかもしれません。Netflixモデルのデジタル教科書提供サービスPerlegoについてWill a Netflix Model Work for Textbooksという記事から紹介します。" #5
              + "{}".format("http://www.the-academic-times.com/2017/09/perlego.html"),

      #''' 6'''  
              "どうして、人はすぐ名前を忘れてしまうのでしょう。今回は、Psychology TodayのWhy We Forget Names (But Not Faces)という記事を紹介したいと思います。" #6
              + "{}".format("http://www.the-academic-times.com/2017/09/why-we-cannot-remember-name-of-others.html"),
        
      #''' 7'''  
              "本来であれば、普通に生活できるものの、アクセシビリティの低いデザインのせいで、個人の自主性と独立性が失われるのです" #7
              + "{}".format("http://www.the-academic-times.com/2017/09/for-whom-design-is-for.html"),
              
      #''' 8'''  
              "キャリアアナリストであるダニエルピンクは、時代遅れの誤ったモチベーションマネジメントが原因だと主張します。今回は、Tedトークス「やる気に関する驚きの科学」をご紹介します。 " #4
              + "{}".format("http://www.the-academic-times.com/2017/07/motivation-version3.html"),
      
      #''' 9'''  
              "今、教育格差が広がっています。特に貧困の再生産などが話題になっていますね。今回は御茶ノ水大学の耳塚寛明による『小学校学力格差に挑む : だれが学力を獲得するのか(<特集>「格差」に挑む)』という研究の紹介です。" #5
              + "{}".format("http://www.the-academic-times.com/2017/05/parentocracy.html"),

      #''' 10'''  
              "今回は、ホーストン大学の社会心理学者Mai-Ly Steers教授による、「みんながキラキラしていると落ち着かない！：フェイスブック利用とうつ症状の関連性について」についてご紹介します。" #6
              + "{}".format("http://www.the-academic-times.com/2017/05/facebook-makes-you-depressed.html"),
        
      #''' 11'''  
              "国際大学グローバル・コミュニケーションセンターの山口真一氏による、『実証分析による炎上の実態と炎上加担者属性の検証』という論文の紹介です。" #7
              + "{}".format("http://www.the-academic-times.com/2017/05/attributes-of-people-who-flame-the-internet.html"),
              
      #''' 12'''  
              "2015年、アメリカの科学者らは暴力的なゲームと、現実世界の暴力：一般的な言説とデータの比較という研究を行いました。" #4
              + "{}".format("http://www.the-academic-times.com/2017/05/videogames-and-crime-rates.html"),
        ]

try:
    tweet = random.choice(tweets) 
    print("以下のツイートを取得しました。ツイートを開始します。：　{}:".format(tweet))
    api.update_status(tweet)
    print("成功しました！")  
except Exception as e:
    print("ツイートに失敗しました:{}".format(e))
