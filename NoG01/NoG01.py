#203213ゆゆゆ

#203211noog

#203105かにかに

#203128bit

#203210れお

#*******************************************************

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

#tkinter（Python UI）のインポート
import tkinter as tk

import tkinter.ttk as ttk
from tkinter import ttk
from tkinter import messagebox

#AI(keras)モデルのインポート
from keras.models import Sequential
from keras.models import load_model

from keras.layers import Dense, Dropout
from keras.utils import np_utils

#AI制作に便利なsklearnのインポート
from sklearn import preprocessing
from sklearn.model_selection import  train_test_split

#AI用配列やデータ格納、計算用のnumpyのインポート
import numpy as np

#YoutubeAPI系と関連のインポート
import datetime
import requests
import json

import isodate
import urllib.request
import urllib.parse

from googleapiclient.discovery import build

#SQLインポート
import psycopg2
from psycopg2 import Error

#画像系インポート
from PIL import ImageTk, Image 
from io import BytesIO

#その他？のインポート
import os





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
    label_thumbnail.pack_forget()

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


#frame1からframe2かframe3
def go_windowX():
    #model lord
    path = 'models/NoGProt.h5'

    model = load_model(path)

    global moviehistorytree
    global moviehistorytreecount
    global channelhistorytree
    global channelhistorytreecount

    global label_thumbnail

    global YOUTUBE_API_KEY

    global URL_input
    global SuspiciousDegree_input

    global cursor

    global test_video_data_x

    global setVideoDatas

    global eva_toInt

    URL = text_input.get("1.0","end")

    if box_a.get()=="URL検索":

        if text_input.get("1.0","end").count('https://www.youtube.com/watch?v') >= 2:
            label_errorfake.pack_forget()
            label_error.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

            messagebox.showerror("Error", "URLが重複している可能性があります。")
            return

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
            return

        elif "https://www.youtube.com/watch?v" in text_input.get("1.0","end"):

            videoid = URL.replace('https://www.youtube.com/watch?v=','').replace('\n','').replace('%0a','')
            if len(videoid) != 11:
                messagebox.showerror("Error", "URLの文字数にエラーがあります")
                return

            frame1.pack_forget()
            frame2.pack(padx = 0 , pady = 0)
            label_error.pack_forget()
            label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

        elif "https://youtu.be/" in text_input.get("1.0","end"):

            videoid = URL.replace('https://youtu.be/','').replace('\n','').replace('%0a','')

            if len(videoid) != 11:
                messagebox.showerror("Error", "URLの文字数にエラーがあります")
                return

            messagebox.showinfo("ok","短縮URLです")

            frame1.pack_forget()
            frame2.pack(padx = 0 , pady = 0)

            label_error.pack_forget()
            label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

        else:
            label_errorfake.pack_forget() 
            label_error.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)          

            messagebox.showerror("Error", "URLに誤りがあります。")
            text_input.delete("1.0","end")
            return

        #11/17追加

        if len(videoid) != 11:
            messagebox.showerror("Error", "URLの文字数にエラーがあります")
            return


        #videoid = URL.replace('https://www.youtube.com/watch?v=','').replace('\n','').replace('%0a','')
   
        print(videoid)

        param = {
                'part': 'snippet,contentDetails,statistics',
                'id': videoid, 
                'key': YOUTUBE_API_KEY
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

            label_title.configure(text="タイトル　→→　" + title)

            thumbnailUrl2 = item["snippet"]["thumbnails"]["high"]["url"]

            response2 = requests.get(thumbnailUrl2)

            img2 = Image.open(BytesIO(response2.content))

            img2resize = img2.resize((1000,750))

            thumbnail2 = ImageTk.PhotoImage(img2resize)

            label_thumbnail = tk.Label(frame2, image=thumbnail2)

            label_thumbnail.image = thumbnail2

            label_thumbnail.pack(padx = 50, pady = 10, after=label_title)
            
            vidViewCount = int(item['statistics']['viewCount'])
            vidLikeCount = int(item['statistics']['likeCount'])

            description = item['snippet']['description'].replace('\'', '')
            vidSecondsAfterAll = int(vidDuration.total_seconds())
            channelName = item["snippet"]["channelTitle"]
            dateUploaded = isodate.parse_datetime(item["snippet"]["publishedAt"])

            dateYear = dateUploaded.year
            dateMonth=dateUploaded.month
            dateDay=dateUploaded.day
            dateHour=dateUploaded.hour

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

            if (len(response["items"]) <= 30):
                messagebox.showerror("Error", "コメント数が30以下なので分析できません。")
                return


            global suspicious_words, unsuspicious_words

            positive_count = 0
            negative_count = 0

            BestGoodCount = 0
            WorstGoodCount = 0

            for itemc in response["items"]:


                comment = itemc["snippet"]["topLevelComment"]

                author = comment["snippet"]["authorDisplayName"]

                likeCount = comment["snippet"]["likeCount"]

                replyCount = itemc["snippet"]["totalReplyCount"]

                comment_text = comment["snippet"]["textDisplay"]

                for a_suspicious_word in suspicious_words:

                    # 釣り動画らしい、怪しい単語が含まれていると、怪しさカウントをプラス１する。
                    if comment_text != None and a_suspicious_word in comment_text:
                        negative_count += 1

                    # 何の単語も含まれていないと、何もせず次のループへ。
                    else:
                        None

                for a_unsuspicious_word in unsuspicious_words:

                    # 釣り動画らしくない、怪しくない単語が含まれていると、怪しさカウントをマイナス１する。
                    if(comment_text != None and a_unsuspicious_word in comment_text):
                        positive_count += 1

                    # 何の単語も含まれていないと、何もせず次のループへ。
                    else:
                        None

            
                if (likeCount >= BestGoodCount):
                    toplevelcomment = comment_text
                    #toplevelcommentauthor = author
                    toplevelcommentlikecount = likeCount
                    toplevelcommentreplycount = replyCount

                if (likeCount <= WorstGoodCount):
                    lastLevelcomment = comment_text
                    #lastLevelcommentauthor = author
                    lastLevelcommentlikecount = likeCount
                    lastLevelcommentreplycount = replyCount

                commentCount += 1

            subscriberCount = int(item['statistics'].get('subscriberCount', vidViewCount/2))

        #AIに予測させる

        positive_word = positive_count/len(response["items"])
        negative_word = negative_count/len(response["items"])

        URL_test = np.array([( (vidLikeCount*100)/vidViewCount, positive_word, negative_word)])

        """
        URL_test = np.concatenate((URL_test,
                                    np.array([(vidViewCount, vidLikeCount
                                    , (vidLikeCount*100)/vidViewCount, vidSecondsAfterAll
                                    , subscriberCount
                                    , toplevelcommentlikecount, toplevelcommentreplycount
                                    , lastLevelcommentlikecount, lastLevelcommentreplycount
                                    )])
        ))
        """







        #scaler = preprocessing.StandardScaler()
        #scaler.fit(URL_test)
        
        
        #x=scaler.transform(URL_test)
        
        #print(x)
        #x_train, x_test = train_test_split(x,test_size=0)
        #SuspiciousDegree=suspiciousDegree, URL="https://www.youtube.com/watch?v="+videoid
        print("URL_test" ,URL_test)

        multiply = 1
        x =  [[round((vidLikeCount*100)/vidViewCount), round(positive_word), round(negative_word)]]
        print("x = ",x)

        x = scaler.transform(x)
        print("x = ",x)

        URL_predict = model.predict(x)

        print("URL_predict = ", URL_predict)

        anzenn = URL_predict[0][0]
        anzenn = anzenn * 100
        suspiciousDegree = URL_predict[0][1]
        suspiciousDegree = suspiciousDegree * 100

        print(anzenn)
        print(suspiciousDegree)
        """
        print(type(URL_test))

        print("URL_test = ", URL_test)

        cursor.execute('SELECT * FROM icebox')

        scaler1 = preprocessing.StandardScaler()
        scaler1.fit(URL_test[:999])

        print("before model predict scaler1 = ", scaler1)

        transform = scaler1.transform(URL_test[:999])
        
        print("before model predict transform = ", transform)
        print("before model predict transform[0][0] = ", transform[0][0])

        URL_predict = model.predict(URL_test[:999])
        """


        """
        max = 0
        maxindex = 0
        for i in range(100):
            ttt = URL_predict[0][i]
            if max < ttt:
                max = ttt
                maxindex = i
            else:
                None

        suspiciousDegree = maxindex
        """

        print("URL_predict == " , URL_predict)
        suspiciousDegree = URL_predict[0][1] * 100
        print(suspiciousDegree)

        global label_dangerlevel

        label_dangerlevel.configure(text="動画の釣り危険度" + str(suspiciousDegree) + "%")


        moviehistorytree.insert(parent='', index=0, iid= moviehistorytreecount,values=(title,text_input.get("1.0","end"), str(suspiciousDegree) + '%'))
        moviehistorytreecount += 1



        cursor.execute("INSERT INTO correctresult VALUES("\
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

        elif "https://www.youtube.com/channel/" in text_input.get("1.0","end"):
            ch = URL.replace('https://www.youtube.com/channel/','').replace('\n','').replace('%0a','')
            if len(ch) != 24:
                messagebox.showerror("Error", "URLの文字数にエラーがあります")
                return

            frame1.pack_forget()
            frame3.pack(padx = 0, pady = 0)
            label_error.pack_forget()
            label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)
            """
            elif "https://www.youtube.com/@" in text_input.get("1.0","end"):
                x = urlopen(URL)
                raw_data = x.read()
                encoding = x.info().get_content_charset('utf8')  # JSON default
                data = json.loads(raw_data.decode(encoding))

                ch = URL.replace('https://www.youtube.com/','').replace('\n','').replace('%0a','')

                messagebox.showinfo("info", "カスタムURLです")
                frame1.pack_forget()
                frame3.pack(padx = 0, pady = 0)
                label_error.pack_forget()
                label_errorfake.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)
            """
        else:
            label_errorfake.pack_forget()
            label_error.pack(padx = 10, pady = 5, expand=1, after=label_inputURL)

            messagebox.showerror("Error", "URLに誤りがあります。")
            text_input.delete("1.0","end")
            return

        #11/22日チャンネル検索機能追加
        import datetime
        global video_ids
        global test_video_data_x

        today = datetime.datetime.now()

        #beforデータ
        ChyearA = today.year
        ChmonthA = today.month
        ChdayA = today.day

        #afterデータ
        ChyearB = ChyearA
        ChmonthB = ChmonthA-1
        ChdayB = ChdayA
        if ChmonthB == 0:
           ChyearB-=1
           ChmonthB = 12

        dtype = [('vidID','<U255'), ('anzenn', float), ('suspic', float)]
        ans = np.array([("chchchchchchchchchchchchchchch", 100, 0)],dtype=dtype)

        #aa = np.array([[0,0],[0,0]])

        test_video_data_x = np.array([[50, 5, 0]])


        for i in range(2):

            setVideoDatas(ch, 50, ChyearB, ChmonthB, ChdayB, ChyearA, ChmonthA, ChdayA)
            ChmonthA-=1
            if ChmonthA == 0:
                ChyearA-=1
                ChmonthA = 12
            else:
                None

            ChmonthB-=1
            if ChmonthB == 0:
                ChyearB-=1
                ChmonthB = 12

        count = 0
        fcount = 0

        print(video_ids)

        for vid in test_video_data_x:
            
            if fcount <= 0:
                fcount+=1
                continue


            URL_test2 = np.array([vid])

            URL_test2 = np.concatenate((URL_test2,
                                    np.array([vid])
            ))

            scaler3 = preprocessing.StandardScaler()
            scaler3.fit(URL_test2)
            videoX=scaler3.transform(URL_test2)

            print("translated videoX = ", videoX)

            URL_predict = model.predict(videoX)
            print("URL_predict = ", URL_predict)

            vidID = video_ids[count]

            anzenn = URL_predict[0][0]
            anzenn = anzenn * 100

            suspiciousDegree = URL_predict[0][1]
            suspiciousDegree = suspiciousDegree * 100

            count+=1                           
           
            ans = np.concatenate((ans, np.array([(vidID, anzenn, suspiciousDegree)],dtype=dtype)))
            #a = np.array(ans, dtype=dtype)
            ans = np.sort(ans, order='anzenn')
            
            print("ans = ", ans)

        SumSus = 0
        onetwothreeCount = 0

        for i in ans:

            id = i[0]
            anzenn = i[1]
            suspiciousDegree = i[2]
            SumSus += suspiciousDegree

            onetwothreeCount += 1

        averageSus= SumSus/len(ans)

        global label_channeldangerlevel

        label_channeldangerlevel.configure(text="チャンネルの釣り危険度" + str(averageSus) + "%")

        videoid = ans[0][0]
        
        param = {
                'part': 'snippet,contentDetails,statistics',
                'id': videoid, 
                'key': YOUTUBE_API_KEY
                }

        target_url = 'https://www.googleapis.com/youtube/v3/videos?' + (urllib.parse.urlencode(param))
        videos_body = json.load(urllib.request.urlopen(urllib.request.Request(target_url)))
        print("videos_body = ", videos_body)

        print(target_url)

        print("forに入りたい")

        channelName = ""

        for item in videos_body['items']:
            print("aa", "for文に入りま")

            channelName = item["snippet"]["channelTitle"]

            vidDuration = isodate.parse_duration(item['contentDetails']['duration'])

            title1 = item['snippet']['title'].replace('\'', '')

            thumbnailUrl1 = item["snippet"]["thumbnails"]["default"]["url"]
            thumbnailUrl2 = item["snippet"]["thumbnails"]["high"]["url"]

            response1 = requests.get(thumbnailUrl1)
            response2 = requests.get(thumbnailUrl2)

            img1 = Image.open(BytesIO(response1.content))
            img2 = Image.open(BytesIO(response2.content))

            img2resize = img2.resize((500,350))

            thumbnail1 = ImageTk.PhotoImage(img1)
            thumbnail2 = ImageTk.PhotoImage(img2resize)

            label_thumbnail2 = tk.Label(label_horizon, image=thumbnail2)

            label_thumbnail2.image = thumbnail2

            label_thumbnail2.pack(padx = 50, pady = 10, side = tk.RIGHT, anchor = tk.CENTER)


        videoid = ans[1][0]    
        
        param = {
                'part': 'snippet,contentDetails,statistics',
                'id': videoid, 
                'key': YOUTUBE_API_KEY
                }

        target_url = 'https://www.googleapis.com/youtube/v3/videos?' + (urllib.parse.urlencode(param))
        videos_body = json.load(urllib.request.urlopen(urllib.request.Request(target_url)))
        print("videos_body = ", videos_body)

        print(target_url)

        print("forに入りたい")
        for item in videos_body['items']:
            print("aa", "for文に入りま")

            vidDuration = isodate.parse_duration(item['contentDetails']['duration'])

            title2 = item['snippet']['title'].replace('\'', '')

            thumbnailUrl1 = item["snippet"]["thumbnails"]["default"]["url"]
            thumbnailUrl2 = item["snippet"]["thumbnails"]["high"]["url"]

            response1 = requests.get(thumbnailUrl1)
            response2 = requests.get(thumbnailUrl2)

            img1 = Image.open(BytesIO(response1.content))
            img2 = Image.open(BytesIO(response2.content))

            img2resize = img2.resize((500,350))

            thumbnail1 = ImageTk.PhotoImage(img1)
            thumbnail2 = ImageTk.PhotoImage(img2resize)

            label_thumbnail3 = tk.Label(label_horizon, image=thumbnail2)

            label_thumbnail3.image = thumbnail2

            label_thumbnail3.pack(padx = 50, pady = 10, side = tk.RIGHT, anchor = tk.CENTER)
           

        videoid = ans[2][0]    

        param = {
                'part': 'snippet,contentDetails,statistics',
                'id': videoid, 
                'key': YOUTUBE_API_KEY
        }

        target_url = 'https://www.googleapis.com/youtube/v3/videos?' + (urllib.parse.urlencode(param))
        videos_body = json.load(urllib.request.urlopen(urllib.request.Request(target_url)))
        print("videos_body = ", videos_body)

        print(target_url)

        print("forに入りたい")
        for item in videos_body['items']:
            print("aa", "for文に入りま")

            vidDuration = isodate.parse_duration(item['contentDetails']['duration'])

            title3 = item['snippet']['title'].replace('\'', '')

            thumbnailUrl1 = item["snippet"]["thumbnails"]["default"]["url"]
            thumbnailUrl2 = item["snippet"]["thumbnails"]["high"]["url"]

            response1 = requests.get(thumbnailUrl1)
            response2 = requests.get(thumbnailUrl2)

            img1 = Image.open(BytesIO(response1.content))
            img2 = Image.open(BytesIO(response2.content))

            img2resize = img2.resize((500,350))

            thumbnail1 = ImageTk.PhotoImage(img1)
            thumbnail2 = ImageTk.PhotoImage(img2resize)

            label_thumbnail4 = tk.Label(label_horizon, image=thumbnail2)

            label_thumbnail4.image = thumbnail2

            label_thumbnail4.pack(padx = 50, pady = 10, side = tk.RIGHT, anchor = tk.CENTER)

            label_channelname.configure(text="チャンネル名　→→　" + channelName)

            label_title1.configure(text = title1)
            label_title2.configure(text = title2)
            label_title3.configure(text = title3)

            label_Sus1.configure(text="危険度：" + str(ans[0][2]))
            label_Sus2.configure(text="危険度：" + str(ans[1][2]))
            label_Sus3.configure(text="危険度：" + str(ans[2][2]))

            channelhistorytree.insert(parent='', index=0, iid= channelhistorytreecount,values=(channelName,text_input.get("1.0","end"), str(averageSus) + "%"))
            channelhistorytreecount += 1

        print(ans[2][0])
        video_ids = []

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

        videoid = URL.replace('https://www.youtube.com/watch?v=','').replace('\n','').replace('%0a','')

    elif("https://youtu.be/" in URL) and (SuspiciousDegree <= 100) and (SuspiciousDegree >= 0):
        messagebox.showinfo("ok", "短縮urlok")
        videoid = URL.replace('https://youtu.be/','').replace('\n','').replace('%0a','')


        videoid = URL.replace('https://www.youtube.com/watch?v=','').replace('/n','').replace('%0a','')
    elif("https://youtu.be/" in URL) and (SuspiciousDegree <= 100) and (SuspiciousDegree >= 0):
        messagebox.showinfo("ok", "短縮urlok")
        videoid = URL.replace('https://youtu.be/','').replace('/n','').replace('%0a','')

    else:
        messagebox.showerror("Error", "URLまたは数字が違います")
        return

    if len(videoid) != 11:
        messagebox.showerror("Error", "URLの文字数にエラーがあります")
        return


    #videoid = URL.replace('https://www.youtube.com/watch?v=','').replace('\n','').replace('%0a','')


   
    print(videoid)
    suspiciousDegree = SuspiciousDegree_input.get("1.0","end")

    param = {
            'part': 'snippet,contentDetails,statistics',
            'id': videoid, 
            'key': YOUTUBE_API_KEY
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
                #toplevelcommentauthor = author
                toplevelcommentlikecount = likeCount
                toplevelcommentreplycount = replyCount

            if (likeCount <= WorstGoodCount):
                lastLevelcomment = comment_text
                #lastLevelcommentauthor = author
                lastLevelcommentlikecount = likeCount
                lastLevelcommentreplycount = replyCount

            commentCount += 1


        #vidDislikeCount = int(item['statistics']['dislikeCount'])
        subscriberCount = int(item['statistics'].get('subscriberCount', vidViewCount/2))

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
                   , "とは", "重要な", "お知らせ", "ベスト", "最", "について。", "どっきり", "ドッキリ", "サプライズ", "えぇ・", "逆"
                   ,"釣り動画", "サムネ詐欺", "釣り", "ごみ", "おもんな", "騙", "びっくり", "茶番", "案件"
                   ,"wrong", "evil", "mystery", "don't know", "doesn't know", "Why", "why", "reason", "retired"
                    , "fishing", "scam", "browser back", "garbage", "stupid", "die", "haa", "huh", "lazy", "tired", "nice", "no needed", "Unnecessary"
                    , "What is", "What's?", "Important", "Announcement", "Best", "Most", "About."
                    ,"fishing video", "thumbnail scam", "fishing", "garbage", "strange", "cheating", "surprise", "farce", "problem"]

#好印象単語登録
unsuspicious_words = ["正し", "義", "善", "良", "わかる", "分かる", "理由が", "りゆうが", "なるほど", "継続", "これからも", "待", "評価"
                   , "必要と", "ありがとう", "有難う", "有り難う", "神"
                   , "まとめ", "考察", "歴代", "便利", "解説", "紹介", "その", "第", "回", "10", "１０", "十", "について、", "について解", "について紹"
                   , "最高", "ありがとう", "うまい", "面白", "好き", "楽しい"
                   , "Right", "Righteous", "Virtue", "Good", "Great", "superb", "Understand", "Understand", "Reason", "Reason"
                   , "I see", "Continue", "From now on", " Wait", "Evaluate"
                   , "necessary", "thank you", "thank you", "thank you", "god"
                   , "Summary", "Consideration", "Successive", "Convenient", "Commentary", "Introduction", "That", "No."
                   , "Time", "10", "ten", "Ten", " About ", "Solution about", "Introduction about"
                   , "Excellent", "Thank you", "God", "Interesting", "Like", "Fun"]

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


"""
test_video_data_x = np.array([[2000, 1000
                        , 50, 300
                        , eva_toInt("うおおおおおおお！！！"), eva_toInt("え・・・？")
                        , 2022, 4, 1, 12
                        , eva_toInt("＾＾"), 800
                        , eva_toInt("大丈夫？？"), 5, 2
                        , eva_toInt("なにこれ？"), 0, 1
                        ]])
"""

test_video_data_x = np.array([[50, 5, 0]])

"""
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
"""
test_video_data_x = np.concatenate((test_video_data_x, np.array([[1, 0.01, 0.5]]) ))


print("^O^", test_video_data_x)

#釣り動画＝1 普通動画＝0 # 2 ＝　ネタ動画
answer_data_y = np.array([0, 1])
#answer_data_y = np.array([0])

video_ids = []

def setVideoDatas(ID, number, yb, mb, db, ya, ma, da):

    global test_video_data_x
   

    global cursor

    global answer_data_y

    global video_ids

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

    print("1")
 
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
            vidCommentsCount = int(item['statistics'].get('commentCount', vidViewCount/100))
            #vidDislikeCount = int(item['statistics']['dislikeCount'])
            vidSubscriberCount = int(item['statistics'].get('subscriberCount', vidViewCount/2))
            vidHiddenSubscriberCount = int(item['statistics'].get('hiddenSubscriberCount', vidViewCount/2))

            vidDuration = isodate.parse_duration(item['contentDetails']['duration'])

            res = youtube.videos().list(id=videoId,part='statistics').execute()

        print(res['items'])

        video_ids = np.append(video_ids, videoId)
        print("unnko",video_ids)
        
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

        print("2")

        #comennntbool = True

        global suspicious_words, unsuspicious_words

        positive_count = 0
        negative_count = 0

        try:

            request = youtube.commentThreads().list(
                part = "snippet",
                videoId=videoId,
                maxResults = 500
            )
            response = request.execute()

            if (len(response["items"]) <= 30):
                messagebox.showerror("Error", "コメント数が30以下なので分析できません。")
                continue

            for item in response["items"]:

                comment = item["snippet"]["topLevelComment"]

                author = comment["snippet"]["authorDisplayName"]

                likeCount = comment["snippet"]["likeCount"]

                replyCount = item["snippet"]["totalReplyCount"]

                comment_text = comment["snippet"]["textDisplay"]

                for a_suspicious_word in suspicious_words:

                    # 釣り動画らしい、怪しい単語が含まれていると、怪しさカウントをプラス１する。
                    if comment_text != None and a_suspicious_word in comment_text:
                        negative_count += 1

                    # 何の単語も含まれていないと、何もせず次のループへ。
                    else:
                        None

                for a_unsuspicious_word in unsuspicious_words:

                    # 釣り動画らしくない、怪しくない単語が含まれていると、怪しさカウントをマイナス１する。
                    if(comment_text != None and a_unsuspicious_word in comment_text):
                        positive_count += 1

                    # 何の単語も含まれていないと、何もせず次のループへ。
                    else:
                        None
 

            
                if (likeCount >= BestGoodCount):
                    toplevelcomment = comment_text
                    #toplevelcommentauthor = author
                    toplevelcommentlikecount = likeCount
                    toplevelcommentreplycount = replyCount
                    BestGoodCount = likeCount

                if (likeCount <= WorstGoodCount):
                    lastLevelcomment = comment_text
                    #lastLevelcommentauthor = author
                    lastLevelcommentlikecount = likeCount
                    lastLevelcommentreplycount = replyCount
                    WorstGoodCount = likeCount
                commentCount += 1

                print("[",author,"]  " , comment_text, "コメ目 → ",commentCount)

        except:
            messagebox.showinfo("情報","コメントが非表示の動画を検出")


        print("\n")

        print("3")

        vidSecondsAfterAll = int(vidDuration.total_seconds())

        subscriberCount = 0

        print(str(vidHiddenSubscriberCount) + "vidHiddenSubscriberCount")
        print(str(vidSubscriberCount) + "vidSubscriberCount")

        if vidHiddenSubscriberCount:
            subscriberCount = vidViewCount
        else:
            subscriberCount = vidSubscriberCount

            print(dateUploaded)
            dateUploaded

        if (vidSubscriberCount==0):
            subscriberCount = vidViewCount / 2

        print("4")

        positive_word = positive_count/len(response["items"])
        negative_word = negative_count/len(response["items"])

        print("response = ", response)

        print("positive_count = ", positive_count)
        print("negative_count = ", negative_count)

        print("positive_word = ", positive_word)
        print("negative_word = ", negative_word)
        
        cursor.execute("INSERT INTO icebox VALUES("\
                        "'{VideoId}', '{Title}', '{Description}', {ViewCount}, {LikeCount}"\
                        ", {VideoLength}, '{ChannelName}', {ChannelSubscribersCount}"\
                        ", {DateYear}, {DateMonth}, {DateDay}, {DateHour}"\
                        ", '{GoodComment}', {GoodCommentGoodCount}, {GoodCommentReplyCount}"\
                        ", '{BadComment}', {BadCommentGoodCount}, {BadCommentReplyCount}"\
                        ", {SuspiciousDegree}, '{URL}', {PositiveWord}, {NegativeWord}) ON CONFLICT DO NOTHING".format(
                            VideoId=videoId, Title=title, Description=description
                            , ViewCount=vidViewCount, LikeCount=vidLikeCount
                            , VideoLength=vidSecondsAfterAll, ChannelName=channelName
                            , ChannelSubscribersCount=subscriberCount
                            , DateYear=dateUploaded.year, DateMonth=dateUploaded.month
                            , DateDay=dateUploaded.day, DateHour=dateUploaded.hour
                            , GoodComment=toplevelcomment, GoodCommentGoodCount=toplevelcommentlikecount, GoodCommentReplyCount=toplevelcommentreplycount
                            , BadComment=lastLevelcomment, BadCommentGoodCount=lastLevelcommentlikecount, BadCommentReplyCount=lastLevelcommentreplycount
                            , SuspiciousDegree="50.111", URL="https://www.youtube.com/watch?v="+videoId, PositiveWord=positive_word, NegativeWord=negative_word
                            )
                       )

        cursor.execute("COMMIT;")

        test_video_data_x = np.concatenate((test_video_data_x, np.array([[(vidLikeCount*100)/vidViewCount, positive_word, negative_word]]) ))
        answer_data_y = np.append(answer_data_y, 0)

        print("5")


"""
        test_video_data_x = np.concatenate((test_video_data_x, np.array([[vidViewCount, vidLikeCount
                                    , (vidLikeCount*100)/vidViewCount, vidSecondsAfterAll
                                    , eva_toInt(title), eva_toInt(description)
                                    , dateUploaded.year, dateUploaded.month, dateUploaded.day, dateUploaded.hour
                                    , eva_toInt(channelName), subscriberCount
                                    , eva_toInt(toplevelcomment), toplevelcommentlikecount, toplevelcommentreplycount
                                    , eva_toInt(lastLevelcomment), lastLevelcommentlikecount, lastLevelcommentreplycount
                                                                        ]])
                                        ))
"""

def TakeCh():

    chid = text_channelIDinput.get("1.0","end").replace('\n','').replace('%0a','')

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
    
    """
    SQLdetas = np.array([[2000, 1000
                        , 50, 300
                        , 800
                        , 5, 2
                        , 0, 1
                        ]])
    """
    SQLdetas = np.array([[50, 5, 0]])

    SQLdetas = np.concatenate((SQLdetas, np.array([[1, 0.01, 0.5]]) ))
    """
    SQLdetas = np.concatenate((SQLdetas, np.array([[150000, 1500
                        , 1, 300
                        , 800
                        , 111, 5
                        , 3, 8
                                                                ]])
                                    ))
    """
    

    labelSQL = np.array([0, 1])

    print("cursor = ", cursor)

    for row in cursor:

        VideoID = row[0]

        Title = row[1]
        print("row title=" , Title)
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
        for x in row:
            print(x)

        if SuspiciousDegree >= 80:
            SuspiciousDegree = 1
        else:
            SuspiciousDegree = 0
        """
        if SuspiciousDegree >= 99:
            SuspiciousDegree = 99
        else:
            None
        """

        positive_rate = row[20]
        negative_rate = row[21]

        SQLdetas = np.concatenate((SQLdetas, np.array([[(LikeCount*100)/ViewCount, positive_rate, negative_rate ]]) ))

        """
        SQLdetas = np.concatenate((SQLdetas, np.array([[ViewCount, LikeCount
                                    , (LikeCount*100)/ViewCount, VideoLength                                  
                                    , ChannelSubscribersCount
                                    , GoodCommentGoodCount, GoodCommentReplyCount
                                    , BadCommentGoodCount, BadCommentReplyCount
                                                                        ]])
                                        ))
        """

        labelSQL = np.append(labelSQL, SuspiciousDegree)


    scaler = preprocessing.StandardScaler()
    scaler.fit(SQLdetas)

    print("scaler = ", scaler)

    print("SQLdetas = ", SQLdetas)

    x=scaler.transform(SQLdetas)

    countA = 105

    last = x[countA]
    print("last ==" , last)

    print("takeCH x = ",x)

    y = np_utils.to_categorical(labelSQL)
    #print(y)
    y_last = y[countA]
    print("y_last ==" , y_last)

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

    x_test = np.concatenate((x_test, np.array([last]) )) 
    y_test = np.concatenate((y_test, np.array([y_last]) )) 

    print("x_test ==" , x_test)
    DoStudy(dostudyCount)




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
 
box_a = combobox = ttk.Combobox(frame1, value=module, width=15, height=20, state="readonly", cursor="dot",font=("Courier", 20, "bold"))
#box_a.option_add("*TCombobox*Listbox.Font", 30)
box_a.current(0)

# ボタン, テキストの設定(text=ボタンに表示するテキスト)

label_horizon1 = tk.Label(frame1,bg="#42b33d")

btn_cry = tk.Button(label_horizon1, text='泣いちゃった',
width = 10,
height = 2,
bg = "Red",
font=("MSゴシック", "20", "bold"),
command = go_window1toX
)

btn_go4 =  tk.Button(label_horizon1, text='旬の釣り動画検索',
width = 15,
height = 2,
font=("MSゴシック", "20", "bold"),
foreground = "Yellow",
bg = "Purple",
command = go_window4
)

btn_go5 =  tk.Button(label_horizon1, text='履歴の表示',
width = 10,
height = 2,
font=("MSゴシック", "20", "bold"),
foreground = "Cyan",
bg = "Green",
command = go_window5
) 

btn_go = tk.Button(frame1, text='検索',
width = 10,
height = 3,
font=("MSゴシック", "20", "bold"),
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

label_dangerlevel = tk.Label(frame2, text="", font=("MSゴシック", "40", "bold"))

label_title = tk.Label(frame2, text="", font=("MSゴシック", "10", "bold"))

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

label_channelname = tk.Label(frame3, text="", font=("MSゴシック", "30", "bold"))

label_channeldangerlevel = tk.Label(frame3, text="チャンネルの釣り危険度XX%", font=("MSゴシック", "40", "bold"))

label_channeldangervideo = tk.Label(frame3, text="釣り危険度の高い動画", font=("MSゴシック", "15", "bold"))

image1 = image1.resize((200,200))

label_horizon = tk.Label(frame3, bg="#42b33d")

label_titlehorizon = tk.Label(frame3, bg="#42b33d")

label_title1 = tk.Label(label_titlehorizon, text="", font=("MSゴシック", "10", "bold"))
label_title2 = tk.Label(label_titlehorizon, text="", font=("MSゴシック", "10", "bold"))
label_title3 = tk.Label(label_titlehorizon, text="", font=("MSゴシック", "10", "bold"))

label_Sushorizon = tk.Label(frame3, bg="#42b33d")

label_Sus1 = tk.Label(label_Sushorizon, text="", font=("MSゴシック", "20", "bold"))

label_Sus2 = tk.Label(label_Sushorizon, text="", font=("MSゴシック", "20", "bold"))

label_Sus3 = tk.Label(label_Sushorizon, text="", font=("MSゴシック", "20", "bold"))

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

label_historydisplay = tk.Label(frame5, text="履歴表示画面", font=("MSゴシック", "30", "bold"))

label_moviehistoryhorizon = tk.Label(frame5)

label_channelhistoryhorizon = tk.Label(frame5)

label_videodangerlevelrankinghorizon = tk.Label(frame5)

label_moviehistory = tk.Label(label_moviehistoryhorizon, text="直近の検索動画", font=("MSゴシック", "30", "bold"))

label_channelhistory = tk.Label(label_channelhistoryhorizon, text="直近の検索チャンネル", font=("MSゴシック", "30", "bold"))

label_videodangerlevelranking = tk.Label(label_videodangerlevelrankinghorizon, text="釣り危険度ランキング", font=("MSゴシック", "30", "bold"))


#表の挿入
#URL検索履歴
# 列の識別名を指定
column = ('MovieTitle','MovieUrl', 'MovieDangerLevel')
# Treeviewの生成
moviehistorytree = ttk.Treeview(label_moviehistoryhorizon, columns=column)
# 列の設定
moviehistorytree.column('#0',width=0, stretch='no')
moviehistorytree.column('MovieTitle', anchor='w', width=400)
moviehistorytree.column('MovieUrl', anchor='w', width=400)
moviehistorytree.column('MovieDangerLevel',anchor='w', width=100)
# 列の見出し設定
moviehistorytree.heading('#0',text='')
moviehistorytree.heading('MovieTitle', text='動画タイトル',anchor='center')
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
channelhistorytree.column('ChannelName', anchor='w', width=300)
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
font=("MSゴシック", "20", "bold"),
foreground = "Cyan",
bg = "Black",
command = go_window5to1
)


#frameX


#横並びに配置するための入れ物(text)を定義する
label_horizonX = tk.Label(frameX,bg="#42b33d")


# ボタン, テキストの設定(text=ボタンに表示するテキスト)

use1 = tk.Button(label_horizonX, text='DBに保存',
width = 25,
height = 10,
font=("MSゴシック", "20", "bold"),
foreground = "Black",
bg = "Cyan",
command = go_windowXtoX1
)

use2 = tk.Button(label_horizonX, text='日付内から取得',
width = 25,
height = 10,
font=("MSゴシック", "20", "bold"),
foreground = "Black",
bg = "Cyan",
command = go_windowXtoX2
)

use3 = tk.Button(label_horizonX, text='AIに学習',
width = 25,
height = 10,
font=("MSゴシック", "20", "bold"),
foreground = "Black",
bg = "Cyan",
command = go_windowXtoX3
)

back = tk.Button(frameX, text='最初に戻る',
width = 10,
height = 3,
font=("MSゴシック", "20", "bold"),
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
width = 30,
height = 5,
font=("MSゴシック", "20", "bold"),
foreground = "Black",
bg = "Cyan",
command = savemovieinfo
)

back_windowX1 = tk.Button(frameX1, text='機能一覧へ',
width = 10,
height = 3,
font=("MSゴシック", "20", "bold"),
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
width = 30,
height = 5,
font=("MSゴシック", "20", "bold"),
foreground = "Black",
bg = "Cyan",
command = TakeCh
)


backX2 = tk.Button(frameX2, text='機能一覧へ',
width = 15,
height = 3,
font=("MSゴシック", "20", "bold"),
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
width = 30,
height = 5,
font=("MSゴシック", "20", "bold"),
foreground = "Black",
bg = "Cyan",
command = takeSQL
)


backX3 = tk.Button(frameX3, text='機能一覧へ',
width = 15,
height = 5,
font=("MSゴシック", "20", "bold"),
foreground = "Black",
bg = "Cyan",
command = go_backX3
)

#ボタンやテキストを配置する位置の設定(frame1)

#1画面目

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

#2画面目
label_URLsearch.pack(padx = 10, pady = 10, expand=1)
label_dangerlevel.pack(padx = 50, pady = 10, expand=1)
label_title.pack(padx = 50, pady = 10, after=label_dangerlevel)
#label_thumbnail.pack(padx = 50, pady = 10)
btn_return.pack(padx = 50, pady = 10, expand=1)

sizegrip2 = ttk.Sizegrip(frame2)
sizegrip2.pack(padx = 5, pady = 5)

#3画面目
label_channelIDsearch.pack(padx = 10, pady = 10, expand=1, side = tk.TOP)
label_channelname.pack(padx = 50, pady = 10, after=label_channelIDsearch)
label_channeldangerlevel.pack(padx = 50, pady = 10, expand=1, side = tk.TOP)

label_horizon.pack(padx = 50, pady = 10, expand=1)
btn_return2.pack(padx = 50, pady = 10, expand=1, side = tk.BOTTOM, anchor = tk.CENTER)
label_channeldangervideo.pack(padx = 50, pady = 10, expand=1, side = tk.BOTTOM, anchor = tk.CENTER)

label_title1.pack(padx = 100, pady = 10, side = tk.RIGHT)
label_title2.pack(padx = 100, pady = 10, side = tk.RIGHT)
label_title3.pack(padx = 100, pady = 10, side = tk.RIGHT)
label_titlehorizon.pack(padx = 50, pady = 10, expand=1)

label_Sus1.pack(padx = 100, pady = 10, side = tk.RIGHT)
label_Sus2.pack(padx = 100, pady = 10, side = tk.RIGHT)
label_Sus3.pack(padx = 100, pady = 10, side = tk.RIGHT)
label_Sushorizon.pack(padx = 50, pady = 10, expand=1)


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


#----------------------------------  YoutubeAPIここまで？ -------------------------------------------------------------------------------


scaler = preprocessing.StandardScaler()
scaler.fit(test_video_data_x)
x=scaler.transform(test_video_data_x)
#print(x)

y = np_utils.to_categorical(answer_data_y,num_classes=2)
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
    model.add(Dense(32, activation='relu', input_dim = 3))
    model.add(Dropout(0.2))

    #隠れ層作成　ニューロン数32　活性化関数＝ReLU　
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))

    #出力層作成　ニューロン数(出力数)=1　活性化関数＝softmax
    model.add(Dense(2, activation='softmax'))
    #model.add(Dense(10))

    #最適化アルゴリズム　= SGD,損失機関=交差エントロピー、尺度＝精度
    model.compile(optimizer='sgd', loss='categorical_crossentropy',metrics=['accuracy'])
    #model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])

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
def DoStudy(count=0):

    global study_times_str
    global study_times_int

    global model
    global path

    model = load_model(path)

    study_times_str = ""

    if count == 0:

        study_times_str = input("\n\n何回学習する...？ [input number and enter, 数字(整数自然数値)を入力！]: ") 
    
        checkIfInt()
    
    study_times_int = int(study_times_str) if count is None else count

    history = model.fit(x_train, y_train, epochs=study_times_int, batch_size=1) #batch_sizeは8(2^3)でもいいかも？

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

