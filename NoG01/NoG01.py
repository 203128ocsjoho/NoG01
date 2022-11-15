#203213ゆゆゆ

#203211noog

#203105かにかに

#203128bit

#203210れお

#*******************************************************

#1

#2


#3


#4

#5
#tkinterのインポート
from argparse import ONE_OR_MORE
from cgitb import text
from multiprocessing.connection import answer_challenge
from pickle import FLOAT
import tkinter as tk

import tensorflow as tf
import numpy as np
import keras as ks

from keras.models import Sequential
from keras.layers import Dense, Dropout

from keras.utils import np_utils
from keras.utils import to_categorical

from sklearn import preprocessing
from sklearn.model_selection import  train_test_split

from keras.models import load_model

import os

'''
#10/21　表出力でやるはず
#import pandas as pd
#import matplotlib.pyplot as plt
'''

'''
#エクセル系
#import openpyxl
#import xlrd
'''

import tkinter.ttk as ttk
from tkinter import Text, Tk, ttk
from tkinter import messagebox

from PIL import ImageTk, Image 

#YoutubeAPI系 インポート
import datetime
import requests
import json
import re

import isodate
import urllib.request
import urllib.parse

#from apiclient.discovery import build
from googleapiclient.discovery import build


import psycopg2
from psycopg2 import Error



YOUTUBE_API_KEY = 'AIzaSyCu7OyzTomXx6rujSKQCzS4aSAjgfBFqB8'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)



try:
    #接続
    connector =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                user="yuyuyu",        #ユーザ
                password="yuyuyu123",  #パスワード
                host="60.66.192.16",       #ホスト名
                port="5432",            #ポート
                dbname="postgres"))    #データベース名

    #カーソル取得
    cursor = connector.cursor()

    cursor.execute("SELECT version();")
    result = cursor.fetchone() 

    print(result[0]+"に接続しています。")


    #cursor.execute('INSERT INTO "Icebox" VALUES({a})'.format(a="a",))
    #row = cursor.fetchone() 
    #print(row)

except(Exception, Error) as error:
    print("PostgreSQLへの接続時のエラーが発生しました",error)

#最後は必ずクローズ
finally:
    None
    #cursor.close()
    #connector.close()



#tkinterを起動
root = tk.Tk()

#メインウィンドウの設定
root.title("釣り動画判別ソフト : メインメニュー")
root.geometry("1920x1080")
root.state("zoomed")

#フレームの作成
#frameの定義
frame1 = tk.Frame(root,height=1080,width=1920, bg="#42b33d")
frame1.propagate(False)

frame2 = tk.Frame(root,height=1080,width=1920, bg="#42b33d")
frame2.propagate(False)

frame3 = tk.Frame(root,height=1080,width=1920, bg="#42b33d")
frame3.propagate(False)

frame4 = tk.Frame(root,height=1080,width=1920, bg="#42b33d")
frame4.propagate(False)

frame5 = tk.Frame(root,height=1080,width=1920, bg="#42b33d")
frame5.propagate(False)

frameX = tk.Frame(root,height=1080,width=1920, bg="#42b33d")
frameX.propagate(False)

frameX1 = tk.Frame(root,height=1080,width=1920, bg="#42b33d")
frameX1.propagate(False)

frameX2 = tk.Frame(root,height=1080,width=1920, bg="#42b33d")
frameX2.propagate(False)

frameX3 = tk.Frame(root,height=1080,width=1920, bg="#42b33d")
frameX3.propagate(False)


#関数定義

cryCount = True
def cry_window():

    global cryCount

    if cryCount == False:
        label_error.pack_forget()
        label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)
    else:
        label_errorfake.pack_forget()
        label_error.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)
        

        messagebox.showinfo("確認", text_input.get("1.0", "end"))
    cryCount = not cryCount


def go_window2():
    #frame1.pack_forget()
    #frame2.pack(padx = 5, pady = 5)


    if text_input.get("1.0","end").count('https://www.youtube.com/watch?v') >= 2:
        text_input.pack_forget()
        btn_go.pack_forget()
        label_error.pack(padx = 50, pady = 5, expand=1)
        text_input.pack(padx = 50, pady = 30, expand=1)
        btn_go.pack(padx = 50, pady = 20, expand=1)

        messagebox.showerror("Error", "URLが重複している可能性があります。")

    elif "https://www.youtube.com/watch?v" in text_input.get("1.0","end"):
        frame1.pack_forget()
        frame2.pack(padx = 5, pady = 5)
        label_error.pack_forget()

    else:
        text_input.pack_forget()
        btn_go.pack_forget()
        label_error.pack(padx = 50, pady = 5, expand=1)
        text_input.pack(padx = 50, pady = 30, expand=1)
        btn_go.pack(padx = 50, pady = 20, expand=1)

        messagebox.showerror("Error", "URLに誤りがあります。")
        text_input.delete("1.0","end")

def go_window3():
    frame1.pack_forget()
    frame3.pack(padx = 0, pady = 0)
    label_error.pack_forget()

def go_window4():
    frame1.pack_forget()
    frame4.pack(padx = 0, pady = 0)
    label_error.pack_forget()

def go_window5():
    frame1.pack_forget()
    frame5.pack(padx = 0, pady = 0)
    label_error.pack_forget()

def go_window1():
    frame2.pack_forget()
    frame1.pack(padx = 0, pady = 0)
    global cryCount
    cryCount = True
    label_error.pack_forget()
    label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

def go_window3to1():
    frame3.pack_forget()
    frame1.pack(ipadx = 0, ipady = 0)
    global cryCount
    cryCount = True
    label_error.pack_forget()
    label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)
    

def go_window4to1():
    frame4.pack_forget()
    frame1.pack(ipadx = 0, ipady = 0)
    global cryCount
    cryCount = True
    label_error.pack_forget()
    label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

def go_window5to1():
    frame5.pack_forget()
    frame1.pack(ipadx = 0, ipady = 0)
    global cryCount
    cryCount = True
    label_error.pack_forget()
    label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)



#frame1からframeX
def go_window1toX():
    frame1.pack_forget()
    frameX.pack(padx = 0, pady = 0)
    label_error.pack_forget()

#frameXからframe1
def go_windowXto1():
    frameX.pack_forget()
    frame1.pack(padx = 0, pady = 0)
    label_error.pack_forget()

#frameXからframeX1
def go_windowXtoX1():
    frameX.pack_forget()
    frameX1.pack(padx = 0, pady = 0)
    label_error.pack_forget()

#frameXからframeX2
def go_windowXtoX2():
    frameX.pack_forget()
    frameX2.pack(padx = 0, pady = 0)
    label_error.pack_forget()
    
    #frameXからframeX3
def go_windowXtoX3():
    frameX.pack_forget()
    frameX3.pack(padx = 0, pady = 0)
    label_error.pack_forget()

#frameX1からframeX
def go_backX1():
    frameX1.pack_forget()
    frameX.pack(padx = 0, pady = 0)
    label_error.pack_forget()

#frameX2からframeX
def go_backX2():
    frameX2.pack_forget()
    frameX.pack(padx = 0, pady = 0)
    label_error.pack_forget()

#frameX3からframeX
def go_backX3():
    frameX3.pack_forget()
    frameX.pack(padx = 0, pady = 0)
    label_error.pack_forget()



def go_windowX():
    if box_a.get()=="URL検索":
         if text_input.get("1.0","end").count('https://www.youtube.com/watch?v') >= 2:
            label_errorfake.pack_forget()
            label_error.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

            messagebox.showerror("Error", "URLが重複している可能性があります。")
         elif "nishikawaokiro" in text_input.get("1.0","end") or "reookiro" in text_input.get("1.0","end"):
            okiro = False
            while okiro == False:
                okiro = messagebox.askyesno("okiro","起きる？")
                if okiro == False:
                    for x in range(100):
                        messagebox.showerror("okiro","起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ")
                else:
                    None

            frame1.pack_forget()
            frameX.pack(padx = 0 , pady = 0)
            label_error.pack_forget()
            label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)
         elif "https://www.youtube.com/watch?v" in text_input.get("1.0","end"):
            frame1.pack_forget()
            frame2.pack(padx = 0 , pady = 0)
            label_error.pack_forget()
            label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

            global moviehistorytree
            global moviehistorytreecount
            moviehistorytree.insert(parent='', index=0, iid= moviehistorytreecount,values=(text_input.get("1.0","end"), 'XX%'))
            moviehistorytreecount += 1


         else:
            label_errorfake.pack_forget() 
            label_error.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)          

            messagebox.showerror("Error", "URLに誤りがあります。")
            text_input.delete("1.0","end")
    elif box_a.get()=="チャンネルID検索":
        if text_input.get("1.0","end").count('https://www.youtube.com/c') >= 2:
            label_error.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)
            label_errorfake.pack_forget()

            messagebox.showerror("Error", "URLが重複している可能性があります。")
        elif "nishikawaokiro" in text_input.get("1.0","end") or "reookiro" in text_input.get("1.0","end"):
            frame1.pack_forget()
            frameX.pack(padx = 0 , pady = 0)
            label_error.pack_forget()
            label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

        elif "https://www.youtube.com/c" in text_input.get("1.0","end"):
            frame1.pack_forget()
            frame3.pack(padx = 0, pady = 0)
            label_error.pack_forget()
            label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

            global channelhistorytree
            global channelhistorytreecount
            moviehistorytree.insert(parent='', index=0, iid= channelhistorytreecount,values=("XXX",text_input.get("1.0","end"), 'XX%'))
            channelhistorytreecount += 1

        else:
            label_errorfake.pack_forget()
            label_error.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

            messagebox.showerror("Error", "URLに誤りがあります。")
            text_input.delete("1.0","end")
    else:
        messagebox.showerror("Error", "予期せぬエラーが発生しました")


def isint(str):  # 整数値を表しているかどうかを判定
    try:
        int(str, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True



def savemovieinfo():


    global YOUTUBE_API_KEY
    global URL_input
    global SuspiciousDegree_input
    global cursor

    URL = URL_input.get("1.0","end")
    if isint(SuspiciousDegree_input.get("1.0","end")):
        SuspiciousDegree = int(SuspiciousDegree_input.get("1.0","end"))
        messagebox.showinfo("Error", "数字ok")
    else:
        print("elsereturn")
        messagebox.showerror("Error", "数字を入力してくれ")
        return None

    
    if ("https://www.youtube.com/watch?v=" in URL) and (SuspiciousDegree <= 100) and (SuspiciousDegree >= 0):
        messagebox.showinfo("ok", "urlok")
<<<<<<< HEAD
        videoid = URL.replace('https://www.youtube.com/watch?v=','').replace('\n','').replace('%0a','')
    elif("https://youtu.be/" in URL) and (SuspiciousDegree <= 100) and (SuspiciousDegree >= 0):
        messagebox.showinfo("ok", "短縮urlok")
        videoid = URL.replace('https://youtu.be/','').replace('\n','').replace('%0a','')
=======
        videoid = URL.replace('https://www.youtube.com/watch?v=','').replace('/n','').replace('%0a','')
    elif("https://youtu.be/" in URL) and (SuspiciousDegree <= 100) and (SuspiciousDegree >= 0):
        messagebox.showinfo("ok", "短縮urlok")
        videoid = URL.replace('https://youtu.be/','').replace('/n','').replace('%0a','')
>>>>>>> 回りだしたあの子と僕の未来が～
    else:
        messagebox.showerror("Error", "URLまたは数字が違います")
        return

    if len(videoid) != 11:
        messagebox.showerror("Error", "URLの文字数にエラーがあります")
        return

<<<<<<< HEAD
    #videoid = URL.replace('https://www.youtube.com/watch?v=','').replace('\n','').replace('%0a','')
=======
   
>>>>>>> 回りだしたあの子と僕の未来が～
    print(videoid)
    suspiciousDegree = SuspiciousDegree_input.get("1.0","end")

    param = {
            'part': 'snippet,contentDetails,statistics',
            'id': videoid, 
            'key': 'AIzaSyCu7OyzTomXx6rujSKQCzS4aSAjgfBFqB8'
            }

    target_url = 'https://www.googleapis.com/youtube/v3/videos?' + (urllib.parse.urlencode(param))
    videos_body = json.load(urllib.request.urlopen(urllib.request.Request(target_url)))
    print("videos_body = ", videos_body)

    print(target_url)

    print("forに入りたい")
    for item in videos_body['items']:
        print("aa", "for文に入りま")

        vidDuration = isodate.parse_duration(item['contentDetails']['duration'])

        title = item['snippet']['title'].replace('\'', '')

        vidViewCount = int(item['statistics']['viewCount'])
        vidLikeCount = int(item['statistics']['likeCount'])

        description = item['snippet']['description'].replace('\'', '')
        vidSecondsAfterAll = int(vidDuration.total_seconds())
        channelName = item["snippet"]["channelTitle"]
        vidSubscriberCount = int(item['statistics'].get('subscriberCount', vidViewCount/2))
        vidHiddenSubscriberCount = int(item['statistics'].get('hiddenSubscriberCount', vidViewCount/2))
        dateUploaded = isodate.parse_datetime(item["snippet"]["publishedAt"])
        commentCount = 0
        toplevelcomment = "いいね（デフォルト）"
        #toplevelcommentauthor = "笑（デフォルト）"
        toplevelcommentlikecount = 3
        toplevelcommentreplycount = 3
        lastLevelcomment = "z"
        #lastLevelcommentauthor = "zz"
        lastLevelcommentlikecount = 1
        lastLevelcommentreplycount = 1

        request = youtube.commentThreads().list(
            part = "snippet",
            videoId=videoid,
            maxResults = 500
        )
        response = request.execute()

        BestGoodCount = 0
        WorstGoodCount = 0
        for itemc in response["items"]:

            comment = itemc["snippet"]["topLevelComment"]

            author = comment["snippet"]["authorDisplayName"]

            likeCount = comment["snippet"]["likeCount"]

            replyCount = itemc["snippet"]["totalReplyCount"]

            comment_text = comment["snippet"]["textDisplay"]

            
            if (likeCount >= BestGoodCount):
                toplevelcomment = comment_text
                toplevelcommentauthor = author
                toplevelcommentlikecount = likeCount
                toplevelcommentreplycount = replyCount

            if (likeCount <= WorstGoodCount):
                lastLevelcomment = comment_text
                lastLevelcommentauthor = author
                lastLevelcommentlikecount = likeCount
                lastLevelcommentreplycount = replyCount

            commentCount += 1



        
        vidCommentsCount = int(item['statistics']['commentCount'])
        #vidDislikeCount = int(item['statistics']['dislikeCount'])
        subscriberCount = int(item['statistics'].get('subscriberCount', vidViewCount/2))
        vidHiddenSubscriberCount = int(item['statistics'].get('hiddenSubscriberCount', vidViewCount/2))
       

        
        #vidDuration = isodate.parse_duration(item['contentDetails']['duration'])

        messagebox.showinfo("aa", "DBmade")

        cursor.execute("INSERT INTO icebox VALUES("\
                            "'{VideoId}', '{Title}', '{Description}', {ViewCount}, {LikeCount}"\
                            ", {VideoLength}, '{ChannelName}', {ChannelSubscribersCount}"\
                            ", {DateYear}, {DateMonth}, {DateDay}, {DateHour}"\
                            ", '{GoodComment}', {GoodCommentGoodCount}, {GoodCommentReplyCount}"\
                            ", '{BadComment}', {BadCommentGoodCount}, {BadCommentReplyCount}"\
                            ", {SuspiciousDegree}, '{URL}') ON CONFLICT DO NOTHING".format(
                                VideoId=videoid, Title=title, Description=description
                                , ViewCount=vidViewCount, LikeCount=vidLikeCount
                                , VideoLength=vidSecondsAfterAll, ChannelName=channelName
                                , ChannelSubscribersCount=subscriberCount
                                , DateYear=dateUploaded.year, DateMonth=dateUploaded.month
                                , DateDay=dateUploaded.day, DateHour=dateUploaded.hour
                                , GoodComment=toplevelcomment, GoodCommentGoodCount=toplevelcommentlikecount, GoodCommentReplyCount=toplevelcommentreplycount
                                , BadComment=lastLevelcomment, BadCommentGoodCount=lastLevelcommentlikecount, BadCommentReplyCount=lastLevelcommentreplycount
                                , SuspiciousDegree=suspiciousDegree, URL="https://www.youtube.com/watch?v="+videoid
                                )
                           )
        cursor.execute("COMMIT;")

        messagebox.showinfo("おあり", "gg")
    messagebox.showinfo("a", "おわりってことだお")




#怪しさ単語登録
suspicious_words = ["?", "？", "違う", "悪", "謎", "わからない", "分からない", "何故", "なぜ", "なんで", "引退"
                   , "釣り", "詐欺", "ブラウザバック", "ごみ", "ゴミ", "しね",  "はあ" ,"はぁ", "だる", "飽き", "いい", "いらない", "不必要"
                   , "とは", "重要な", "お知らせ", "ベスト", "最", "について。"]

#好印象単語登録
unsuspicious_words = ["正し", "義", "善", "良", "わかる", "分かる", "理由が", "りゆうが", "なるほど", "継続", "これからも", "待", "評価"
                   , "必要と", "ありがとう", "有難う", "有り難う", "神"
                   , "まとめ", "考察", "歴代", "便利", "解説", "紹介", "その", "第", "回", "10", "１０", "十", "について、", "について解", "について紹"]

count = 5 #怪しさカウント
count_count = 1 #カウントを何回やったかのカウント
video_count = 1 #何ビデオ目のカウントをやっているかのカウント
#文字を評価値の数字にする何かプロセス
def eva_toInt(string):
    
    count = 5 #怪しさカウント初期化
    global count_count
    global video_count

    #実装予定

    for a_suspicious_word in suspicious_words:

        # 釣り動画らしい、怪しい単語が含まれていると、怪しさカウントをプラス１する。
        if string != None and a_suspicious_word in string:
            count += 1
            print("怪しい単語発見(video_count = ", str(video_count), ", 何カウント目 = ", str(count_count), ", +1)")

        # 何の単語も含まれていないと、何もせず次のループへ。
        else:
            None


    for a_unsuspicious_word in unsuspicious_words:

        # 釣り動画らしくない、怪しくない単語が含まれていると、怪しさカウントをマイナス１する。
        if(string != None and a_unsuspicious_word in string):
            count -= 1
            print("好印象単語発見(video_count = ", str(video_count), ", 何カウント目 = ", str(count_count), ", -1)")

        # 何の単語も含まれていないと、何もせず次のループへ。
        else:
            None
 
    print("video_count = ", str(video_count), ", 何カウント目 = ", str(count_count), ", 怪しさ = ", str(count), " → 次のカウントする変数へ。\n")
    
    count_count += 1

    if (count_count % 5 == 1):
        video_count += 1

    return count



#たくさんの項目数、順番で、それぞれ何を意味しているか。　上、英語　下、日本語
"""
ViewCount, LikeCount
, LikeRate([LikeCount*100]/ViewCount), VideoLength(sec)
, Title, Description
, DateYear, DateMonth, DateDay, DateHour
, ChannelName, ChannelSubscribersCount
, GoodComment, LikeCountofGoodComment, ReplyCountofGoodComment
, BadComment, LikeCountofBadComment, ReplyCountofBadComment
"""
"""
再生数, グッド数
, グッド率([グッド数*100]/再生数), 動画時間（秒）
, タイトル名, 詳細文
, 投稿年, 投稿月, 投稿日, 投稿時間
, チャンネル名, チャンネル登録者数
, （比較的）評価の高いコメント, （比較的）グッドコメントのグッド数, （比較的）グッドコメントの返信数
, （比較的）評価の低いコメント, （比較的）バッドコメントのグッド数, （比較的）バッドコメントの返信数
"""




test_video_data_x = np.array([[2000, 1000
                        , 50, 300
                        , eva_toInt("うおおおおおおお！！！"), eva_toInt("え・・・？")
                        , 2022, 4, 1, 12
                        , eva_toInt("＾＾"), 800
                        , eva_toInt("大丈夫？？"), 5, 2
                        , eva_toInt("なにこれ？"), 0, 1
                        ]])


test_video_data_x = np.concatenate((test_video_data_x, np.array([[100, 2
                        , 2, 60
                        , eva_toInt("は？？"), eva_toInt("きれそう")
                        , 2022, 4, 4, 5
                        , eva_toInt("登録よろしく！！"), 5
                        , eva_toInt("引退しろ！！！"), 2, 1
                        , eva_toInt("次郎、今度野球いこうぜ！"), 1, 2
                                                                ]])
                                    ))


print("OwO", test_video_data_x)

test_video_data_x = np.concatenate((test_video_data_x, np.array([[30000, 3000
                        , 10, 480
                        , eva_toInt("よろしくおねがいします！！"), eva_toInt("趣味は化粧と裁縫とネイルです！( ^)o(^ )")
                        , 2022, 5, 1, 12
                        , eva_toInt("カニちゃん(カニザン)のお化粧備忘録チャンネル"), 3000
                        , eva_toInt("動画内の化粧品まとめ:\n<br>SK-2 税込￥29800\n<br>ニベア 税込￥1980"), 88, 5
                        , eva_toInt("私と同じくらいかわいいですね。"), 0, 8
                                                                ]])
                                    ))
                        

test_video_data_x = np.concatenate((test_video_data_x, np.array([[150000, 1500
                        , 1, 300
                        , eva_toInt("じゃんけんの勝ち方、、、徹底解説します。"), eva_toInt("明日から勝率１００パー間違いねぇぜ！")
                        , 2022, 4, 1, 9
                        , eva_toInt("令和のギャンブラー田中一郎の明日から使えるヤバい技チャンネル"), 800
                        , eva_toInt("ネタかと思った。\n<br>でも顔がマジやん。。"), 111, 5
                        , eva_toInt("この動画のおかげで彼女できました！田中一郎に感謝！！。"), 3, 8
                                                                ]])
                                    ))

test_video_data_x = np.concatenate((test_video_data_x, np.array([[240000, 4800
                        , 2, 630
                        , eva_toInt("Youtuber、やめます！"), eva_toInt("これで終わりだっ・・。\n<br>今までありがとうございました。")
                        , 2022, 7, 7, 3
                        , eva_toInt("ピカル(Pikaru)"), 180000
                        , eva_toInt("この動画は釣り動画、詐欺動画です。ブラウザバックをお勧めします。"), 155, 5
                        , eva_toInt("ごみ！\n\n<br><br><br><br><br><br><br><br>しね！"), 5, 5
                                                                ]])
                                    ))


print("^O^", test_video_data_x)


#釣り動画＝1 普通動画＝0 # 2 ＝　ネタ動画
answer_data_y = np.array([0, 0, 0, 1, 1])
#answer_data_y = np.array([0])

'''
for item in range(searchVideosNumbers):
    answer_data_y = np.append(answer_data_y, 0)
    print(answer_data_y)
'''


def setVideoDatas(ID, number, yb, mb, db, ya, ma, da):

    global test_video_data_x
   

    global cursor

    global answer_data_y

    print("globalglobal", test_video_data_x)

    #dayB = datetime.date.fromisoformat(dateB1)
    tb = datetime.date(yb, mb, db)
    dayB = datetime.datetime.strftime(tb, '%Y-%m-%dT%H:%M:%S.%fZ')

    #dayA = datetime.date.fromisoformat(dateA1)
    ta = datetime.date(ya, ma, da)
    dayA = datetime.datetime.strftime(ta, '%Y-%m-%dT%H:%M:%S.%fZ')

    search_response = youtube.search().list(
    part='snippet',
    #part='id,snippet,contentDetails,player,recordingDetails,statistics,status,topicDetails',
    #fields='items(id,snippet(title,description,publishedAt),contentDetails(duration),statistics(viewCount,likeCount,dislikeCount,commentCount))'
    order='rating',
    type='video',
    regionCode='JP',
    maxResults=number,
    channelId=ID,
    publishedAfter=dayB,
    publishedBefore=dayA,
    ).execute()


    video_ids = []

    videoCountForAPI = 0
    commentCount = 0

    for item in search_response['items'][:number]:
    
        videoCountForAPI += 1

        title = item['snippet']['title'].replace('\'', '')
        description = item['snippet']['description'].replace('\'', '')

        videoId = item["id"]["videoId"]
        url = 'https://www.youtube.com/watch?v=%s' % videoId
        thumbnailUrl1 = item["snippet"]["thumbnails"]["default"]["url"]
        thumbnailUrl2 = item["snippet"]["thumbnails"]["high"]["url"]
        dateUploaded = isodate.parse_datetime(item["snippet"]["publishedAt"])
        channelName = item["snippet"]["channelTitle"]
        videoId = item['id']['videoId']

        param = {
            'part': 
            'id,snippet,contentDetails,player,recordingDetails,statistics,status,topicDetails',
            'id': videoId, 
            'key': YOUTUBE_API_KEY
            }

        target_url = 'https://www.googleapis.com/youtube/v3/videos?' + \
        (urllib.parse.urlencode(param))
        videos_body = json.load(urllib.request.urlopen(urllib.request.Request(target_url)))
        print("videos_body = ", videos_body)
        for item in videos_body['items']:

            vidViewCount = int(item['statistics']['viewCount'])
            vidLikeCount = int(item['statistics']['likeCount'])
            vidCommentsCount = int(item['statistics']['commentCount'])
            #vidDislikeCount = int(item['statistics']['dislikeCount'])
            vidSubscriberCount = int(item['statistics'].get('subscriberCount', vidViewCount/2))
            vidHiddenSubscriberCount = int(item['statistics'].get('hiddenSubscriberCount', vidViewCount/2))

            vidDuration = isodate.parse_duration(item['contentDetails']['duration'])

            res = youtube.videos().list(id=videoId,part='statistics').execute()


        '''
        param2 = {
            'part': 
            'id,snippet,contentDetails,player,recordingDetails,statistics,status,topicDetails',
            'id': "UCaminwG9MTO4sLYeC3s6udA",
            }

        target_url2 = 'https://www.googleapis.com/youtube/v3/channels' + \
        (urllib.parse.urlencode(param2))
        channel_body = json.load(urllib.request.urlopen(urllib.request.Request(target_url2)))

        for item in channel_body['items']:

            #vidSubscriberCount = int(item['statistics']['subscriberCount'])
            vidHiddenSubscriberCount = int(item['statistics']['hiddenSubscriberCount'])

            vidDuration = isodate.parse_duration(item['contentDetails']['duration'])

            res = youtube.videos().list(id=videoId,part='statistics').execute()

        '''

        print(res['items'])

        video_ids.append(videoId)
        request = youtube.commentThreads().list(
            part = "snippet",
            videoId=videoId,
            maxResults = 500
        )
        response = request.execute()

  
        print("タイトル = [", title , "]")
        print("詳細文　＝　[", description , "]")
        print("チャンネルID = [", channelName , "]")
        print("VideoURL = [", url , "]")
        print("投稿時間 = [", dateUploaded , "]")
        print("サムネURL1 = [", thumbnailUrl1 , "]")
        print("サムネURL2 = [", thumbnailUrl2 , "]\n")
        print("videoCountForAPI = [",videoCountForAPI, "]\n")
  
        commentCount = 0
        toplevelcomment = "いいね（デフォルト）"
        #toplevelcommentauthor = "笑（デフォルト）"
        toplevelcommentlikecount = 3
        toplevelcommentreplycount = 3
        lastLevelcomment = "z"
        #lastLevelcommentauthor = "zz"
        lastLevelcommentlikecount = 1
        lastLevelcommentreplycount = 1


        BestGoodCount = 0
        WorstGoodCount = 0
        for item in response["items"]:

            comment = item["snippet"]["topLevelComment"]

            author = comment["snippet"]["authorDisplayName"]

            likeCount = comment["snippet"]["likeCount"]

            replyCount = item["snippet"]["totalReplyCount"]

            comment_text = comment["snippet"]["textDisplay"]

            
            if (likeCount >= BestGoodCount):
                toplevelcomment = comment_text
                toplevelcommentauthor = author
                toplevelcommentlikecount = likeCount
                toplevelcommentreplycount = replyCount
                BestGoodCount = likeCount

            if (likeCount <= WorstGoodCount):
                lastLevelcomment = comment_text
                lastLevelcommentauthor = author
                lastLevelcommentlikecount = likeCount
                lastLevelcommentreplycount = replyCount
                WorstGoodCount = likeCount
            commentCount += 1

            print("[",author,"]  " , comment_text, "コメ目 → ",commentCount)


        print("\n")

        '''
        vidMinutes = re.findall(r'T.*M',vidDuration)
        vidMinutesAfter = vidMinutes[1:-1]
        vidSeconds = re.findall(r'M.*S',vidDuration)
        vidSecondsAfter = vidSeconds[1:-1]
        vidSecondsAfterAll = 60 * vidMinutesAfter + vidSecondsAfter
        '''
        vidSecondsAfterAll = int(vidDuration.total_seconds())

        #vidViewCount = res['items']['viewCount']
        #vidLikeCount = res['items']['likeCount']
        #vidDislikeCount = res['items']['dislikeCount']
        subscriberCount = 0
        print(str(vidHiddenSubscriberCount) + "vidHiddenSubscriberCount")
        print(str(vidSubscriberCount) + "vidSubscriberCount")
        if vidHiddenSubscriberCount:
            subscriberCount = vidViewCount
        else:
            subscriberCount = vidSubscriberCount

            ''', vidDislikeCount'''
            ''', (vidDislikeCount*100)/vidViewCount'''

            print(dateUploaded)
            dateUploaded

        if (vidSubscriberCount==0):
            subscriberCount = vidViewCount / 2


        '''
        forprint = np.array([np.array([vidViewCount, vidLikeCount
                                    , (vidLikeCount*100)/vidViewCount, vidSecondsAfterAll
                                    , eva_toInt(title), eva_toInt(description)
                                    , dateUploaded.year, dateUploaded.month, dateUploaded.day, dateUploaded.hour
                                    , eva_toInt(channelName), subscriberCount
                                    , eva_toInt(toplevelcomment), eva_toInt(lastLevelcomment)
                                    ])])

        print("testetetetetetet", forprint)
        '''
        

        
        cursor.execute("INSERT INTO icebox VALUES("\
                        "'{VideoId}', '{Title}', '{Description}', {ViewCount}, {LikeCount}"\
                        ", {VideoLength}, '{ChannelName}', {ChannelSubscribersCount}"\
                        ", {DateYear}, {DateMonth}, {DateDay}, {DateHour}"\
                        ", '{GoodComment}', {GoodCommentGoodCount}, {GoodCommentReplyCount}"\
                        ", '{BadComment}', {BadCommentGoodCount}, {BadCommentReplyCount}"\
                        ", {SuspiciousDegree}, '{URL}') ON CONFLICT DO NOTHING".format(
                            VideoId=videoId, Title=title, Description=description
                            , ViewCount=vidViewCount, LikeCount=vidLikeCount
                            , VideoLength=vidSecondsAfterAll, ChannelName=channelName
                            , ChannelSubscribersCount=subscriberCount
                            , DateYear=dateUploaded.year, DateMonth=dateUploaded.month
                            , DateDay=dateUploaded.day, DateHour=dateUploaded.hour
                            , GoodComment=toplevelcomment, GoodCommentGoodCount=toplevelcommentlikecount, GoodCommentReplyCount=toplevelcommentreplycount
                            , BadComment=lastLevelcomment, BadCommentGoodCount=lastLevelcommentlikecount, BadCommentReplyCount=lastLevelcommentreplycount
                            , SuspiciousDegree="50.111", URL="https://www.youtube.com/watch?v="+videoId
                            )
                       )

        '''
        " SET Title=excluded.Title, Description=excluded.Description, ViewCount=excluded.'upd', LikeCount=excluded.'upd'"\
                        ", VideoLength=excluded.'upd', ChannelName=excluded.'upd', ChannelSubscribersCount=excluded.'upd'"\
                        ", GoodComment=excluded.'upd', BadComment=excluded.'upd', DateYear=excluded.upd', DateMonth=excluded.'upd', DateDay=excluded.'upd', DateHour=excluded.'upd';"
        '''
        

        cursor.execute("COMMIT;")


        test_video_data_x = np.concatenate((test_video_data_x, np.array([[vidViewCount, vidLikeCount
                                    , (vidLikeCount*100)/vidViewCount, vidSecondsAfterAll
                                    , eva_toInt(title), eva_toInt(description)
                                    , dateUploaded.year, dateUploaded.month, dateUploaded.day, dateUploaded.hour
                                    , eva_toInt(channelName), subscriberCount
                                    , eva_toInt(toplevelcomment), toplevelcommentlikecount, toplevelcommentreplycount
                                    , eva_toInt(lastLevelcomment), lastLevelcommentlikecount, lastLevelcommentreplycount
                                                                        ]])
                                        ))

        answer_data_y = np.append(answer_data_y, 0)



def TakeCh():
    global setVideoDatas
    chid =text_channelIDinput.get("1.0","end").replace('\n','').replace('%0a','')

    if len(chid) == 24:
        None
    else:
        print(len(chid))
        messagebox.showerror("Error", "IDが違うぞ☆")
        return None

    if isint(moviecountinput.get("1.0","end")):
        moviecount = int(moviecountinput.get("1.0","end"))
        messagebox.showinfo("Error", "数字ok")

    else:
        print("elsereturn")
        messagebox.showerror("Error", "数字を入力してくれ")
        return None

   
    setVideoDatas(chid, moviecount, int(year_b.get()), int(manth_b.get()), int(day_b.get()), int(year_a.get()), int(manth_a.get()), int(day_a.get()))

def takeSQL():

    global x_train, x_test, y_train, y_test

    global count_count
    count_count = 0
    global video_count
    video_count = 0

    global cursor

    if isint(text_inputlearningcount.get("1.0","end")):
        dostudyCount = int(text_inputlearningcount.get("1.0","end"))
        messagebox.showinfo("Error", "数字ok")

    else:
        print("elsereturn")
        messagebox.showerror("Error", "数字を入力してくれ")
        return None

    cursor.execute('SELECT * FROM icebox')
    
    SQLdetas = np.array([[2000, 1000
                        , 50, 300
                        , eva_toInt("うおおおおおおお！！！"), eva_toInt("え・・・？")
                        , 2022, 4, 1, 12
                        , eva_toInt("＾＾"), 800
                        , eva_toInt("大丈夫？？"), 5, 2
                        , eva_toInt("なにこれ？"), 0, 1
                        ]])

    SQLdetas = np.concatenate((SQLdetas, np.array([[150000, 1500
                        , 1, 300
                        , eva_toInt("じゃんけんの勝ち方、、、徹底解説します。"), eva_toInt("明日から勝率１００パー間違いねぇぜ！")
                        , 2022, 4, 1, 9
                        , eva_toInt("令和のギャンブラー田中一郎の明日から使えるヤバい技チャンネル"), 800
                        , eva_toInt("ネタかと思った。\n<br>でも顔がマジやん。。"), 111, 5
                        , eva_toInt("この動画のおかげで彼女できました！田中一郎に感謝！！。"), 3, 8
                                                                ]])
                                    ))
    

    labelSQL = np.array([0 ,1])

    for row in cursor:
        VideoID = row[0]
        Title = row[1]
        Description = row[2]
        ViewCount = int(row[3])
        LikeCount = int(row[4])
        VideoLength = int(row[5])
        ChannelName = row[6]
        ChannelSubscribersCount = int(row[7])
        DateYear = int(row[8])
        DateMonth = int(row[9])
        DateDay = int(row[10])
        DateHour = int(row[11])
        GoodComment = row[12]
        GoodCommentGoodCount = int(row[13])
        GoodCommentReplyCount = int(row[14])
        BadComment = row[15]
        BadCommentGoodCount = int(row[16])
        BadCommentReplyCount = int(row[17])
        SuspiciousDegree = float(row[18])
        URL = row[19]

        if SuspiciousDegree >= 0.8:
            SuspiciousDegree = 1
        else:
            SuspiciousDegree = 0

        
        SQLdetas = np.concatenate((SQLdetas, np.array([[ViewCount, LikeCount
                                    , (LikeCount*100)/ViewCount, VideoLength
                                    , eva_toInt(Title), eva_toInt(Description)
                                    , DateYear, DateMonth, DateDay, DateHour
                                    , eva_toInt(ChannelName), ChannelSubscribersCount
                                    , eva_toInt(GoodComment), GoodCommentGoodCount, GoodCommentReplyCount
                                    , eva_toInt(BadComment), BadCommentGoodCount, BadCommentReplyCount
                                                                        ]])
                                        ))

        

        labelSQL = np.append(labelSQL, SuspiciousDegree)


    scaler = preprocessing.StandardScaler()
    scaler.fit(SQLdetas)
    x=scaler.transform(SQLdetas)
    #print(x)

    y = np_utils.to_categorical(labelSQL)
    #print(y)

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

    

    DoStudy(dostudyCount)

        
   
        


"""
def close_frame1():
    frame1.destroy()
def close_frame2():
    frame2.destroy()
def raise_frame(frame):
    frame.tkraise()
"""


#frame1

# ラベル表示
label_title = tk.Label(frame1, text="Youtube 釣り動画判別", font=("MSゴシック", "20", "bold"))

#label_desc = tk.Label(frame1, text="(選択肢ボタン)\n(URL検索)\nor(チャンネルID検索)", font=("MSゴシック", "12", "bold"))

label_inputURL = tk.Label(frame1, text="URLを入力↓", font=("MSゴシック", "12", "bold"))

label_error = tk.Label(frame1, text="URLに誤りがあります！！",font=("MSゴシック", "10", "bold"),
                            foreground='linen',background='red')

label_errorfake = tk.Label(frame1,bg="#42b33d")

#ドロップダウンボックス

module = ('URL検索', 'チャンネルID検索')
 
box_a = combobox = ttk.Combobox(frame1, value=module, width=80, height=120, state="readonly", cursor="dot")
box_a.option_add("*TCombobox*Listbox.Font", 30)
box_a.current(0)

# ボタン, テキストの設定(text=ボタンに表示するテキスト)
"""
btn_go = tk.Button(frame1, text='Go',
width = 10,
height = 3,
foreground = "Black",
bg = "Cyan",
command = go_window2
)
"""

label_horizon1 = tk.Label(frame1,bg="#42b33d")


btn_cry = tk.Button(label_horizon1, text='泣いちゃった',
width = 10,
height = 2,
bg = "Red",
command = go_window1toX
)

btn_go4 =  tk.Button(label_horizon1, text='旬の釣り動画検索',
width = 15,
height = 2,
foreground = "Yellow",
bg = "Purple",
command = go_window4
)

btn_go5 =  tk.Button(label_horizon1, text='履歴の表示',
width = 10,
height = 2,
foreground = "Cyan",
bg = "Green",
command = go_window5
) 

btn_go = tk.Button(frame1, text='Go',
width = 10,
height = 3,
foreground = "Black",
bg = "Cyan",
command = go_windowX
)

text_input = tk.Text(frame1, 
width = 85,
height = 3,
pady = 3,
wrap = tk.NONE,
foreground = "Black",
bg = "Cyan",
)


# frame2

label_URLsearch = tk.Label(frame2, text="URL検索", font=("MSゴシック", "15", "bold"))

label_dangerlevel = tk.Label(frame2, text="動画の釣り危険度XX%", font=("MSゴシック", "40", "bold"))

path_thumbnail = "pictures"
if os.path.isdir(path_thumbnail):
    None
else:
    os.makedirs('pictures/')

image1 = Image.open(path_thumbnail + "/pic1.png")
test = ImageTk.PhotoImage(image1)


label_thumbnail = tk.Label(frame2, image=test)
label_thumbnail.image = test

btn_return = tk.Button(frame2, text='最初の画面に戻る',
width = 15,
height = 3,
foreground = "Cyan",
bg = "Black",
command = go_window1
)

#frame3

label_channelIDsearch = tk.Label(frame3, text="チャンネルID検索", font=("MSゴシック", "15", "bold"))

label_channeldangerlevel = tk.Label(frame3, text="チャンネルの釣り危険度XX%", font=("MSゴシック", "40", "bold"))

label_channeldangervideo = tk.Label(frame3, text="釣り危険度の高い動画", font=("MSゴシック", "15", "bold"))

image1 = image1.resize((200,200))

label_horizon = tk.Label(frame3, bg="#42b33d")

test2 = ImageTk.PhotoImage(image1)
label_thumbnail2 = tk.Label(label_horizon, image=test2)
label_thumbnail2.image = test2

#image1 = image1.resize((150,150))
test3 = ImageTk.PhotoImage(image1)
label_thumbnail3 = tk.Label(label_horizon, image=test3)
label_thumbnail3.image = test3

#image1 = image1.resize((100,100))
test4= ImageTk.PhotoImage(image1)
label_thumbnail4 = tk.Label(label_horizon, image=test4)
label_thumbnail4.image = test4

btn_return2 = tk.Button(frame3, text='最初の画面に戻る',
width = 15,
height = 3,
foreground = "Blue",
bg = "White",
command = go_window3to1
)

#frame4

label_trendyvideo = tk.Label(frame4, text="旬の釣り動画検索", font=("MSゴシック", "15", "bold"))

label_trendyvideodangerlevel = tk.Label(frame4, text="動画の危険度XX%", font=("MSゴシック", "40", "bold"))

image1 = image1.resize((600,400))
test5= ImageTk.PhotoImage(image1)
label_thumbnail5 = tk.Label(frame4, image=test5)
label_thumbnail5.image = test5

btn_return3 = tk.Button(frame4, text='最初の画面に戻る',
width = 15,
height = 3,
foreground = "Cyan",
bg = "Black",
command = go_window4to1
)

#frame5

label_historydisplay = tk.Label(frame5, text="履歴表示画面", font=("MSゴシック", "15", "bold"))

label_moviehistoryhorizon = tk.Label(frame5)

label_channelhistoryhorizon = tk.Label(frame5)

label_videodangerlevelrankinghorizon = tk.Label(frame5)

label_moviehistory = tk.Label(label_moviehistoryhorizon, text="直近の検索動画", font=("MSゴシック", "30", "bold"))

label_channelhistory = tk.Label(label_channelhistoryhorizon, text="直近の検索チャンネル", font=("MSゴシック", "30", "bold"))

label_videodangerlevelranking = tk.Label(label_videodangerlevelrankinghorizon, text="釣り危険度ランキング", font=("MSゴシック", "30", "bold"))


#表の挿入
#URL検索履歴
# 列の識別名を指定
column = ('MovieUrl', 'MovieDangerLevel')
# Treeviewの生成
moviehistorytree = ttk.Treeview(label_moviehistoryhorizon, columns=column)
# 列の設定
moviehistorytree.column('#0',width=0, stretch='no')
moviehistorytree.column('MovieUrl', anchor='w', width=400)
moviehistorytree.column('MovieDangerLevel',anchor='w', width=100)
# 列の見出し設定
moviehistorytree.heading('#0',text='')
moviehistorytree.heading('MovieUrl', text='動画URL',anchor='center')
moviehistorytree.heading('MovieDangerLevel', text='動画の危険度', anchor='center')
# レコードの追加
moviehistorytreecount = 0
#moviehistorytree.insert(parent='', index=, iid=0 ,values=("https://www.youtube.com/watch?v=aaaa", '50%'))
#moviehistorytree.insert(parent='', index='end', iid=1 ,values=("https://www.youtube.com/watch?v=bbbb",'25%'))
#moviehistorytree.insert(parent='', index='end', iid=2, values=("https://www.youtube.com/watch?v=cccc",'80%'))
#moviehistorytree.insert(parent='', index='end', iid=3, values=("https://www.youtube.com/watch?v=dddd",'77%'))
#moviehistorytree.insert(parent='', index='end', iid=4, values=("https://www.youtube.com/watch?v=eeee",'XX%'))

#項番の設定（URL検索履歴）
# 列の識別名を指定
column = ('count')
# Treeviewの生成
counttree = ttk.Treeview(label_moviehistoryhorizon, columns=column)
# 列の設定
counttree.column('#0',width=0, stretch='no')
counttree.column('count', anchor='center', width=20)
# 列の見出し設定
counttree.heading('#0',text='')
counttree.heading('count', text='',anchor='center')
# レコードの追加
counttree.insert(parent='', index="end", iid=0 ,values=("1"))
counttree.insert(parent='', index="end", iid=1 ,values=("2"))
counttree.insert(parent='', index="end", iid=2 ,values=("3"))
counttree.insert(parent='', index="end", iid=3 ,values=("4"))
counttree.insert(parent='', index="end", iid=4 ,values=("5"))
counttree.insert(parent='', index="end", iid=5 ,values=("6"))
counttree.insert(parent='', index="end", iid=6 ,values=("7"))
counttree.insert(parent='', index="end", iid=7 ,values=("8"))
counttree.insert(parent='', index="end", iid=8 ,values=("9"))
counttree.insert(parent='', index="end", iid=9 ,values=("10"))


#チャンネルID検索履歴
# 列の識別名を指定
column = ('ChannelName', 'ChannelId', 'ChannelDangerLevel')
# Treeviewの生成
channelhistorytree = ttk.Treeview(label_channelhistoryhorizon, columns=column)
# 列の設定
channelhistorytree.column('#0',width=0, stretch='no')
channelhistorytree.column('ChannelName', anchor='w', width=100)
channelhistorytree.column('ChannelId',anchor='w', width=400)
channelhistorytree.column('ChannelDangerLevel',anchor='w', width=100)
# 列の見出し設定
channelhistorytree.heading('#0',text='')
channelhistorytree.heading('ChannelName', text='チャンネル名',anchor='center')
channelhistorytree.heading('ChannelId', text='チャンネルID', anchor='center')
channelhistorytree.heading('ChannelDangerLevel', text='チャンネル危険度', anchor='center')
# レコードの追加
channelhistorytreecount = 0
#channelhistorytree.insert(parent='', index='end', iid=0 ,values=("プロたん","https://www.youtube.com/c/aaaa", '50%'))
#channelhistorytree.insert(parent='', index='end', iid=1 ,values=("非課金TV","https://www.youtube.com/c/bbbb",'25%'))
#channelhistorytree.insert(parent='', index='end', iid=2, values=("ピカル","https://www.youtube.com/c/cccc",'80%'))
#channelhistorytree.insert(parent='', index='end', iid=3, values=("らファえル","https://www.youtube.com/c/dddd",'77%'))
#channelhistorytree.insert(parent='', index='end', iid=4, values=("XX","https://www.youtube.com/c/eeee",'XX%'))

#項番の設定（チャンネルID検索履歴）
# 列の識別名を指定
column = ('count')
# Treeviewの生成
counttree1 = ttk.Treeview(label_channelhistoryhorizon, columns=column)
# 列の設定
counttree1.column('#0',width=0, stretch='no')
counttree1.column('count', anchor='center', width=20)
# 列の見出し設定
counttree1.heading('#0',text='')
counttree1.heading('count', text='',anchor='center')
# レコードの追加
counttree1.insert(parent='', index="end", iid=0 ,values=("1"))
counttree1.insert(parent='', index="end", iid=1 ,values=("2"))
counttree1.insert(parent='', index="end", iid=2 ,values=("3"))
counttree1.insert(parent='', index="end", iid=3 ,values=("4"))
counttree1.insert(parent='', index="end", iid=4 ,values=("5"))
counttree1.insert(parent='', index="end", iid=5 ,values=("6"))
counttree1.insert(parent='', index="end", iid=6 ,values=("7"))
counttree1.insert(parent='', index="end", iid=7 ,values=("8"))
counttree1.insert(parent='', index="end", iid=8 ,values=("9"))
counttree1.insert(parent='', index="end", iid=9 ,values=("10"))


#危険度ランキング
# 列の識別名を指定
column = ('DangerLevelRanking', 'MovieTitle','MovieUrl', 'MovieDangerLevel')
# Treeviewの生成
dangerlevelrankingtree = ttk.Treeview(label_videodangerlevelrankinghorizon, columns=column)
# 列の設定
dangerlevelrankingtree.column('#0',width=0, stretch='no')
dangerlevelrankingtree.column('DangerLevelRanking', anchor='center', width=100)
dangerlevelrankingtree.column('MovieTitle', anchor='w', width=100)
dangerlevelrankingtree.column('MovieUrl',anchor='w', width=400)
dangerlevelrankingtree.column('MovieDangerLevel',anchor='w', width=100)
# 列の見出し設定
dangerlevelrankingtree.heading('#0',text='')
dangerlevelrankingtree.heading('DangerLevelRanking', text='順位',anchor='center')
dangerlevelrankingtree.heading('MovieTitle', text='動画タイトル', anchor='center')
dangerlevelrankingtree.heading('MovieUrl', text='動画URL',anchor='center')
dangerlevelrankingtree.heading('MovieDangerLevel', text='動画の危険度', anchor='center')
# レコードの追加
dangerlevelrankingtree.insert(parent='', index='end', iid=0 ,values=("1位", "a","https://www.youtube.com/watch?v", '90%'))
dangerlevelrankingtree.insert(parent='', index='end', iid=1 ,values=("2位", "a","https://www.youtube.com/watch?v",'87%'))
dangerlevelrankingtree.insert(parent='', index='end', iid=2, values=("3位", "a","https://www.youtube.com/watch?v",'80%'))
dangerlevelrankingtree.insert(parent='', index='end', iid=3, values=("4位", "a","https://www.youtube.com/watch?v",'77%'))
dangerlevelrankingtree.insert(parent='', index='end', iid=4, values=("5位", "a","https://www.youtube.com/watch?v",'71%'))


btn_return4 = tk.Button(frame5, text='最初の画面に戻る',
width = 15,
height = 3,
foreground = "Cyan",
bg = "Black",
command = go_window5to1
)


#frameX


#横並びに配置するための入れ物(text)を定義する
label_horizonX = tk.Label(frameX,bg="#42b33d")


# ボタン, テキストの設定(text=ボタンに表示するテキスト)
"""
btn_go = tk.Button(frame1, text='Go',
width = 10,
height = 3,
foreground = "Black",
bg = "Cyan",
command = go_window2
)
"""

use1 = tk.Button(label_horizonX, text='Go機能1',
width = 50,
height = 10,
foreground = "Black",
bg = "Cyan",
command = go_windowXtoX1
)

use2 = tk.Button(label_horizonX, text='Go機能2',
width = 50,
height = 10,
foreground = "Black",
bg = "Cyan",
command = go_windowXtoX2
)

use3 = tk.Button(label_horizonX, text='Go機能3',
width = 50,
height = 10,
foreground = "Black",
bg = "Cyan",
command = go_windowXtoX3
)

back = tk.Button(frameX, text='最初に戻る',
width = 10,
height = 3,
foreground = "Black",
bg = "Cyan",
command = go_windowXto1
)


#frameX1
label_horizonX1 = tk.Label(frameX1,bg="#42b33d")
label_horizonY1 = tk.Label(frameX1,bg="#42b33d")

label_URLinput = tk.Label(label_horizonX1, text="動画URLを入力してください", font=("MSゴシック", "20", "bold"))

label_SuspiciousDegree = tk.Label(label_horizonY1, text="怪しさ度を入力してください", font=("MSゴシック", "20", "bold"))

URL_input = tk.Text(label_horizonX1, 
width = 85,
height = 3,
pady = 3,
wrap = tk.NONE,
foreground = "Black",
bg = "Cyan",
)

SuspiciousDegree_input = tk.Text(label_horizonY1, 
width = 85,
height = 3,
pady = 3,
wrap = tk.NONE,
foreground = "Black",
bg = "Cyan",
)

save_date = tk.Button(frameX1, text='保存します',
width = 100,
height = 15,
foreground = "Black",
bg = "Cyan",
command = savemovieinfo
)

back_windowX1 = tk.Button(frameX1, text='機能一覧へ',
width = 10,
height = 3,
foreground = "Black",
bg = "Cyan",
command = go_backX1
)



#frameX2
label_channelID = tk.Label(frameX2, text="チャンネルIDを入力してください", font=("MSゴシック", "15", "bold"))

text_channelIDinput = tk.Text(frameX2, 
width = 50,
height = 3,
pady = 3,
wrap = tk.NONE,
foreground = "Black",
bg = "Cyan",
)


label_moviecounttext = tk.Label(frameX2, text="取得する動画の数を入力する", font=("MSゴシック", "15", "bold"))

label_beforedaystext = tk.Label(frameX2, text="開始日付を設定(yyyy/mm/dd)", font=("MSゴシック", "15", "bold"))

label_afterdaystext = tk.Label(frameX2, text="終了日付を設定(yyyy/mm/dd)", font=("MSゴシック", "15", "bold"))



label_horizonX2 = tk.Label(frameX2,bg="#42b33d")

"""
befor_daysinput = tk.Text(label_horizonX2, 
width = 50,
height = 3,
pady = 3,
wrap = tk.NONE,
foreground = "Black",
bg = "Cyan",
)

after_daysinput = tk.Text(label_horizonX2, 
width = 50,
height = 3,
pady = 3,
wrap = tk.NONE,
foreground = "Black",
bg = "Cyan",
)
"""

moviecountinput = tk.Text(frameX2, 
width = 50,
height = 3,
pady = 3,
wrap = tk.NONE,
foreground = "Black",
bg = "Cyan",
)

beforebox_horizon = tk.Label(frameX2,bg="#42b33d")



module_beforeyear = []
for i in range(30):
    module_beforeyear.append(1998 + i)

 
year_b = combobox = ttk.Combobox(beforebox_horizon, value=module_beforeyear, width=80, height=120, state="readonly", cursor="dot")
year_b.option_add("*TCombobox*Listbox.Font", 30)
year_b.current(0)
print(module_beforeyear)
"""
scrollbar = ttk.Scrollbar(
    frameX2,
    orient=tk.VERTICAL,
    command=beforebox_year.yview)
beforebox_year['yscrollcommand'] = scrollbar.set
scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
"""

module_beforemonth = ('01', '02','03','04','05','06','07','08','09','10','11','12')

manth_b = combobox = ttk.Combobox(beforebox_horizon, value=module_beforemonth, width=80, height=120, state="readonly", cursor="dot")
manth_b.option_add("*TCombobox*Listbox.Font", 30)
manth_b.current(0)

module_beforeday = []

for i in range(30):
  module_beforeday.append(1 + i)
 
day_b = combobox = ttk.Combobox(beforebox_horizon, value=module_beforeday, width=80, height=120, state="readonly", cursor="dot")
day_b.option_add("*TCombobox*Listbox.Font", 30)
day_b.current(0)


afterbox_horizon = tk.Label(frameX2,bg="#42b33d")

module_afteryear = []
for i in range(30):
    module_afteryear.append(1998 + i)
 
year_a = combobox = ttk.Combobox(afterbox_horizon, value=module_afteryear, width=80, height=120, state="readonly", cursor="dot")
year_a.option_add("*TCombobox*Listbox.Font", 30)
year_a.current(0)

module = ('01', '02','03','04','05','06','07','08','09','10','11','12')
 
manth_a = combobox = ttk.Combobox(afterbox_horizon, value=module, width=80, height=120, state="readonly", cursor="dot")
manth_a.option_add("*TCombobox*Listbox.Font", 30)
manth_a.current(0)


module_afterday = []
for i in range(30):
  module_afterday.append(1 + i)
 
day_a = combobox = ttk.Combobox(afterbox_horizon, value=module_afterday, width=80, height=120, state="readonly", cursor="dot")
day_a.option_add("*TCombobox*Listbox.Font", 30)
day_a.current(0)

datasave = tk.Button(frameX2, text='データを保存',
width = 100,
height = 15,
foreground = "Black",
bg = "Cyan",
command = TakeCh
)




backX2 = tk.Button(frameX2, text='機能一覧へ',
width = 20,
height = 8,
foreground = "Black",
bg = "Cyan",
command = go_backX2
)




#frameX3
label_learninghorizon = tk.Label(frameX3,bg="#42b33d")


label_learningcount = tk.Label(label_learninghorizon, text="回数を指定", font=("MSゴシック", "15", "bold"))

text_inputlearningcount = tk.Text(label_learninghorizon, 
width = 50,
height = 3,
pady = 3,
wrap = tk.NONE,
foreground = "Black",
bg = "Cyan",
)


learning = tk.Button(frameX3, text=' 学習させる',
width = 100,
height = 20,
foreground = "Black",
bg = "Cyan",
command = takeSQL
)


backX3 = tk.Button(frameX3, text='機能一覧へ',
width = 20,
height = 8,
foreground = "Black",
bg = "Cyan",
command = go_backX3
)

#ボタンやテキストを配置する位置の設定(frame1)

"""
label_title.place(x=350, y=50)
label_desc.place(x=410, y=115)
label_inputURL.place(x=440, y=200)
label_error.place(x=100, y=50)
text_input.place(x=210, y=255)
#text_input.insert(0, "https://www.youtube.com/watch?v=5qWYfTlAJsg")
btn_go.place(x=450, y=325)
btn_cry.place(x=900, y=20)
"""


#1画面目

#btn_cry.pack(pady = 0, anchor = tk.NE, expand=1)

#btn_go4.pack(pady = 0, anchor = tk.NE, expand=1)
btn_cry.pack(padx = 10, pady = 0, side = tk.RIGHT)
btn_go4.pack(padx = 10, pady = 0, side = tk.RIGHT)
btn_go5.pack(padx = 10, pady = 0, side = tk.RIGHT)
label_horizon1.pack(padx = 50, pady = 10, expand=1)

label_title.pack(padx = 50, pady = 40, expand=1)

box_a.pack(padx = 10, pady = 0, expand=1)

#label_desc.pack(padx = 50, pady = 35, expand=1)
label_inputURL.pack(padx = 10, pady = 5, expand=1)

label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

#label_error.pack(padx = 50, pady = 10, expand=1)
text_input.pack(padx = 50, pady = 20, expand=1)
btn_go.pack(padx = 50, pady = 20, expand=1)


#自動リサイズできるお
sizegrip1 = ttk.Sizegrip(frame1)
sizegrip1.pack(padx = 5, pady = 5)

#frame1.pack(ipadx = 300, ipady = 220)
frame1.pack(padx = 0, pady = 0)
#ipadyを大きくするとバグる（多分画面の大きさの問題）


#ボタンやテキストを配置する位置の設定(frame2)
"""
label_URLsearch.place(x=100, y=50)
label_dangerlevel.place(x=250, y=70)
btn_return.place(x=350, y=450)
"""

#2画面目
label_URLsearch.pack(padx = 10, pady = 10, expand=1)
label_dangerlevel.pack(padx = 50, pady = 10, expand=1)
label_thumbnail.pack(padx = 50, pady = 10)
btn_return.pack(padx = 50, pady = 10, expand=1)

sizegrip2 = ttk.Sizegrip(frame2)
sizegrip2.pack(padx = 5, pady = 5)

#3画面目
label_channelIDsearch.pack(padx = 10, pady = 10, expand=1, side = tk.TOP)
label_channeldangerlevel.pack(padx = 50, pady = 10, expand=1, side = tk.TOP)
label_thumbnail2.pack(padx = 50, pady = 10, side = tk.RIGHT, anchor = tk.CENTER)
label_thumbnail3.pack(padx = 50, pady = 10, side = tk.RIGHT, anchor = tk.CENTER)
label_thumbnail4.pack(padx = 50, pady = 10, side = tk.RIGHT, anchor = tk.CENTER)
label_horizon.pack(padx = 50, pady = 10, expand=1)
btn_return2.pack(padx = 50, pady = 10, expand=1, side = tk.BOTTOM, anchor = tk.CENTER)
label_channeldangervideo.pack(padx = 50, pady = 10, expand=1, side = tk.BOTTOM, anchor = tk.CENTER)


sizegrip3 = ttk.Sizegrip(frame3)
sizegrip3.pack(padx = 5, pady = 5)

#4画面目
label_trendyvideo.pack(padx = 10, pady = 10, expand=1)
label_trendyvideodangerlevel.pack(padx = 50, pady = 10, expand=1)
label_thumbnail5.pack(padx = 50, pady = 10)
btn_return3.pack(padx = 50, pady = 10, expand=1)

sizegrip4 = ttk.Sizegrip(frame4)
sizegrip4.pack(padx = 5, pady = 5)

#5画面目
label_historydisplay.pack(padx=0, pady=0)

moviehistorytree.pack(padx=0, pady=0, side = tk.RIGHT)
counttree.pack(padx=0, pady=0, side = tk.RIGHT)
label_moviehistory.pack(padx=0, pady=0, side = tk.RIGHT)
label_moviehistoryhorizon.pack(padx = 0, pady = 10, expand=1)

channelhistorytree.pack(padx=0, pady=0, side = tk.RIGHT)
counttree1.pack(padx=0, pady=0, side = tk.RIGHT)
label_channelhistory.pack(padx=0, pady=0, side = tk.RIGHT)
label_channelhistoryhorizon.pack(padx = 0, pady = 10, expand=1)


dangerlevelrankingtree.pack(padx=0, pady=0, side = tk.RIGHT)
label_videodangerlevelranking.pack(padx=0, pady=0, side = tk.RIGHT)
label_videodangerlevelrankinghorizon.pack(padx = 0, pady = 10, expand=1)

btn_return4.pack(padx = 50, pady = 30, expand=1)


sizegrip5 = ttk.Sizegrip(frame5)
sizegrip5.pack(padx = 5, pady = 5)

#X画面目
use1.pack(padx = 10, pady = 0, side = tk.LEFT)
use2.pack(padx = 10, pady = 0, side = tk.LEFT)
use3.pack(padx = 10, pady = 0, side = tk.LEFT)
label_horizonX.pack(padx = 50, pady = 10, expand=1)

back.pack(padx = 50, pady = 40, expand=1, anchor='e')

#X1画面目
label_URLinput.pack(padx = 10, pady = 10, side = tk.LEFT)
URL_input.pack(padx = 10, pady = 10, side = tk.LEFT)
label_horizonX1.pack(padx = 50, pady = 40, expand=1)

label_SuspiciousDegree.pack(padx = 10, pady = 0, side = tk.LEFT)
SuspiciousDegree_input.pack(padx = 10, pady = 0, side = tk.LEFT)
label_horizonY1.pack(padx = 50, pady = 10, expand=1)

save_date.pack (padx = 50, pady = 40, expand=1)

back_windowX1.pack (padx = 50, pady = 40, expand=1, anchor='e')



#X2画面目
label_channelID.pack(padx = 50, pady = 40, expand=1)

text_channelIDinput.pack(padx = 0, pady = 0, expand=1)

label_moviecounttext.pack(padx = 50, pady = 40, expand=1)


#befor_daysinput.pack(padx = 50, pady = 0, expand=1, side = tk.RIGHT)
#after_daysinput.pack(padx = 50, pady = 0, expand=1, side = tk.RIGHT)
moviecountinput.pack(padx = 50, pady = 0, expand=1)

label_beforedaystext.pack(padx = 50, pady = 40, expand=1)

year_b.pack(padx = 50, pady = 0, expand=1, side = tk.LEFT)
manth_b.pack(padx = 50, pady = 0, expand=1, side = tk.LEFT)
day_b.pack(padx = 50, pady = 0, expand=1, side = tk.LEFT)
beforebox_horizon.pack(padx = 20, pady = 10, expand=1)

label_afterdaystext.pack(padx = 50, pady = 40, expand=1)

year_a.pack(padx = 50, pady = 0, expand=1, side = tk.LEFT)
manth_a.pack(padx = 50, pady = 0, expand=1, side = tk.LEFT)
day_a.pack(padx = 50, pady = 0, expand=1, side = tk.LEFT)
afterbox_horizon.pack(padx = 20, pady = 10, expand=1)

datasave.pack(padx = 50, pady = 0, expand=1)
backX2.pack(padx = 50, pady = 0, expand=1,  anchor='e')




#X3画面目
text_inputlearningcount.pack(padx = 50, pady = 40, expand=1, side = tk.RIGHT)
label_learningcount.pack(padx = 50, pady = 40, expand=1, side = tk.RIGHT)
label_learninghorizon.pack(padx = 50, pady = 40, expand=1)

learning.pack(padx = 0, pady = 0, expand=1)
backX3.pack(padx = 50, pady = 0, expand=1, anchor='e')


#raise_frame(frame1)
#raise_frame(frame2)

"""
label_URLsearch.grid(row = 0, column = 0, sticky=tkinter.EW)
label_dangerlevel.grid(row = 1, column = 1, sticky=tkinter.EW)
btn_return.grid(row = 2, column = 2, sticky=tkinter.EW)
label_dangerlevel.grid_remove()
"""

"""
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=0)
"""



'''
# 足し算サンプル（使えるかもしれんから残しとく）
a = tf.constant(1234)
b = tf.constant(5000)
add_op = a + b
tf.print(add_op)
'''

'''
# numpytest　ナムパイテスト　後で(10/21)使うはず
temp = np.array([10, 15, 20, 25, 30])
ice  = np.array([20, 22, 20, 32, 30])
plt.scatter(temp, ice)
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
# numpytest ナムパイテスト 複数　配列をランダムで作成
data = np.random.randint(low=0, high=5, size=10)
'''


print("\n(1)起動！起動！！！！\n")


print("\n(2)終わりってことだよぉ！(GUI終了)\n")
print(box_a)

#----------------------------------  ここまでGUI   ------------------------------------------------------------------------------------


print("\n(3)【モデルとか、データ定義始め！】\n")



#-------------------------------------------------------データ定義---------------------------------------------------------

"""
"""

"""
YOUTUBE_API_KEY = 'AIzaSyCu7OyzTomXx6rujSKQCzS4aSAjgfBFqB8'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def get_channel_videos(channel_id):
    
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos


def get_videos_stats(video_ids):
    stats = []
    for i in range(0, len(video_ids), 50):
        res = youtube.videos().list(id=','.join(video_ids[i:i+50]),
                                   part='statistics').execute()
        stats += res['items']
        
    return stats


videos = get_channel_videos('UCaminwG9MTO4sLYeC3s6udA')
video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], videos))
stats = get_videos_stats(video_ids)

len(stats)

res = youtube.videos().list(id=videos[0]['snippet']['resourceId']['videoId'],part='statistics').execute()
res['items']

"""

#['items']['statistics']['likeCount']

#most_disliked = sorted(stats, key=lambda x:int(x['statistics']['likeCount']), reverse=False)
#most_disliked

#for video in most_disliked:
#    print(video['id'], video['statistics']['dislikeCount'])

#---------------------------------------------------------- Step 1 to 2 ---------------------------------




"""

setVideoDatas('UCl4e200EZm7NXq_iaYSXfeg', 50, 2022, 6, 1, 2022, 11, 11)
answer_data_y[len(answer_data_y)-1] = 1
print(test_video_data_x)
"""

print("(4)【モデル定義終わり！】\n")


#----------------------------------  YoutubeAPIここまで？ -------------------------------------------------------------------------------
"""
"""




scaler = preprocessing.StandardScaler()
scaler.fit(test_video_data_x)
x=scaler.transform(test_video_data_x)
#print(x)

y = np_utils.to_categorical(answer_data_y)
#print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)


path0 = 'models'
path = 'models/NoGProt.h5'

is_file0 = os.path.isdir(path0)
is_file = os.path.isfile(path)

print("(5)【モデル定義終わり！】\n")


# モデルを格納するためのフォルダが存在しているか確認。 なければ作る。
if is_file0:
    print("\n(5.5)folder exists")
else:
    print("\n(5.5)folder not exists")
    os.makedirs('models/')   

print("\n")


# モデルファイルが存在しているか確認。 なければ作りながらやる。
if is_file:

    model = load_model(path)

    print("\n(6)Load Model\n")
else:
    print("\n(6)Start Making Model\n")

    model = Sequential()

    #入力層作成　ニューロン数32　活性化関数＝ReLU　入力数＝18
    model.add(Dense(32, activation='relu',input_dim =18))
    model.add(Dropout(0.4))

    #隠れ層作成　ニューロン数32　活性化関数＝ReLU　
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.4))

    #出力層作成　ニューロン数(出力数)=1　活性化関数＝softmax
    model.add(Dense(2, activation='softmax'))

    #最適化アルゴリズム　= SGD,損失機関=交差エントロピー、尺度＝精度
    model.compile(optimizer='sgd', loss='categorical_crossentropy',metrics=['accuracy'])

    print(model.summary())
    model.save(path)



study_times_str = "0" # グローバル変数 何回学習するか String
study_times_int = 0 # グローバル変数 何回学習するか Integer
def checkIfInt(): # 入力された学習回数が数字で入力されたか確認する
    
    global study_times_str

    if isint(study_times_str): # 数字なら何もせずに続ける
        None
    else:
        study_times_str = input("\n数字(整数自然数値)以外が入力されました。もう一度入力してください。"
                                + "\n\n何回学習する？ [input number and enter, 数字を入力！]: ")
        checkIfInt()

# 学習させるための関数（繰り返しできるように作った）
def DoStudy(count):

    global study_times_str
    global study_times_int

    global model
    global path

    model = load_model(path)

    study_times_str = ""

    if count is None:

        study_times_str = input("\n\n何回学習する...？ [input number and enter, 数字(整数自然数値)を入力！]: ") 
    
        checkIfInt()
    
    study_times_int = int(study_times_str) if count is None else count

    history = model.fit(x_train, y_train, epochs=study_times_int, batch_size=10) #batch_sizeは8(2^3)でもいいかも？

    loss, accuracy = model.evaluate(x_test,y_test)
    print("\n\n誤差: [",loss,"], 精度: [",accuracy, "*100%]")

    print("\n\n現在の予測 x_test: \n", model.predict(x_test[:999]))
    print("\n\n現在の予測 x_train: \n", model.predict(x_train[:9]))
    print("\n\ny_test: \n", y_test[:999])
    print("\n\ny_train: \n", y_train[:9])

    print("\n\nhistory = ", history)

    model.save(path)

    loss, accuracy = model.evaluate(x_test,y_test)
    print("\n\n誤差: [",loss,"], 精度: [",accuracy, "*100%]")

    print("\n\n現在の予測 x_test: \n", model.predict(x_test[:999]))
    print("\n\n現在の予測 x_train: \n", model.predict(x_train[:9]))

    print("\n\ny_test: \n", y_test[:999])
    print("\n\ny_train: \n", y_train[:9])



# もう一回学習するかコマンド入力させる関数
def yes_no_input():

    choice = input("\n\nもう一回学習する..？？ [y/N, はい/いいえ]: ").lower()

    if choice in ['y', ' y', 'ye', 'yes', 'はい']:
        return True
    elif choice in ['n', ' n', 'no', 'いいえ']:
        return False



root.mainloop() #なんかわからんけどGUIをループして起動するやつ

#cursor.close()
#connector.close()

DoStudy() # 一回目の学習を行う


# 二回目以降は、選択させる。
while(yes_no_input()):
    DoStudy()


model.save(path) #モデルを保存

print("\n(7)終わりってことだよぉ！(すべての最後―終わり―)\n")

