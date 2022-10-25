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
#from apiclient.discovery import build


#tkinterを起動
root = tk.Tk()

#メインウィンドウの設定
root.title("釣り動画判別ソフト : メインメニュー")
root.geometry("1600x900")

#フレームの作成

frame1 = tk.Frame(root,height=900,width=1600)

frame2 = tk.Frame(root,height=900,width=1600)

cryCount = 1
def cry_window():

    global cryCount

    if cryCount % 2 == 0:
        label_error.pack_forget()
    else:
        text_input.pack_forget()
        btn_go.pack_forget()
        label_error.pack(padx = 50, pady = 5, expand=1)
        text_input.pack(padx = 50, pady = 30, expand=1)
        btn_go.pack(padx = 50, pady = 20, expand=1)

        messagebox.showinfo("確認", text_input.get("1.0", "end"))

    cryCount += 1

def go_window2():
    frame1.pack_forget()
    frame2.pack(padx = 5, pady = 5)


def go_window1():
    frame2.pack_forget()
    frame1.pack(padx = 5, pady = 5)

def close_frame1():
    frame1.destroy()

def close_frame2():
    frame2.destroy()

def raise_frame(frame):
    frame.tkraise()

# ラベル表示
label_title = tk.Label(frame1, text="Youtube 釣り動画判別", font=("MSゴシック", "20", "bold"))

label_desc = tk.Label(frame1, text="(選択肢ボタン)\n(URL検索)\nor(チャンネルID検索)", font=("MSゴシック", "12", "bold"))

label_inputURL = tk.Label(frame1, text="URLを入力↓", font=("MSゴシック", "12", "bold"))

label_error = tk.Label(frame1, text="URLに誤りがあります！！",font=("MSゴシック", "11", "bold"),
                            foreground='linen',background='red')

# ボタン, テキストの設定(text=ボタンに表示するテキスト)
btn_go = tk.Button(frame1, text='Go',
width = 10,
height = 3,
foreground = "Black",
bg = "Cyan",
command = go_window2
)

text_input = tk.Text(frame1, 
width = 85,
height = 3,
pady = 3,
wrap = tk.NONE,
foreground = "Black",
bg = "Cyan",
)

btn_cry = tk.Button(frame1, text='泣いちゃった',
width = 10,
height = 2,
bg = "Red",
command = cry_window
)

# frame2
label_URLsearch = tk.Label(frame2, text="URL検索", font=("MSゴシック", "10", "bold"))

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

btn_cry.pack(pady = 30, anchor = tk.NE, expand=1)

label_title.pack(padx = 50, pady = 40, expand=1)

label_desc.pack(padx = 50, pady = 35, expand=1)
label_inputURL.pack(padx = 50, pady = 5, expand=1)
#label_error.pack(padx = 50, pady = 10, expand=1)
text_input.pack(padx = 50, pady = 30, expand=1)
btn_go.pack(padx = 50, pady = 20, expand=1)

#自動リサイズできるお
sizegrip1 = ttk.Sizegrip(frame1)
sizegrip1.pack(padx = 5, pady = 5)

frame1.pack(padx = 5, pady = 5)

#ボタンやテキストを配置する位置の設定(frame2)
"""
label_URLsearch.place(x=100, y=50)

label_dangerlevel.place(x=250, y=70)

btn_return.place(x=350, y=450)
"""

#2画面目
label_URLsearch.pack(padx = 10, pady = 10, expand=1)
label_dangerlevel.pack(padx = 50, pady = 10, expand=1)
label_thumbnail.pack(padx = 50, pady = 50)
btn_return.pack(padx = 50, pady = 10, expand=1)

sizegrip2 = ttk.Sizegrip(frame1)
sizegrip2.pack(padx = 5, pady = 5)

raise_frame(frame1)
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
root.mainloop() #なんかわからんけどGUIをループして起動するやつ

print("\n(2)終わりってことだよぉ！(GUI終了)\n")


#----------------------------------  ここまでGUI   ------------------------------------------------------------------------------------


print("\n(3)【モデルとか、データ定義始め！】\n")


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
ViewCount, LikeCount, (DislikeCount)
, LikeRate([LikeCount*100]/ViewCount), (DislikeRate), VideoLength(sec)
, Title, Description
, DateYear, DateMonth, DateDay, DateAMorPM(0,1)
, ChannelName, ChannelSubscribersCount
, GoodComment, BadComment
"""
"""
再生数, グッド数, (バッド数)
, グッド率([グッド数*100]/再生数), (バッド率), 動画時間（秒）
, タイトル名, 詳細文
, 投稿年, 投稿月, 投稿日, 投稿時間が午前か午後か(0,1)
, チャンネル名, チャンネル登録者数
, 評価の高いコメント, 評価の低いコメント
"""

test_video_data_x = np.array([

            np.array([2000, 1000, 500
                        , 50, 25, 300
                        , eva_toInt("うおおおおおおお！！！"), eva_toInt("え・・・？")
                        , 2022, 4, 1, 1
                        , eva_toInt("＾＾"), 800
                        , eva_toInt("大丈夫？？"), eva_toInt("なにこれ？")]),

            np.array([100, 2, 60
                        , 2, 60, 60
                        , eva_toInt("は？？"), eva_toInt("きれそう")
                        , 2022, 4, 4, 0
                        , eva_toInt("登録よろしく！！"), 5
                        , eva_toInt("引退しろ！！！"), eva_toInt("次郎、今度野球いこうぜ！")]),

            np.array([30000, 3000, 30
                        , 10, 1, 480
                        , eva_toInt("よろしくおねがいします！！"), eva_toInt("趣味は化粧と裁縫とネイルです！( ^)o(^ )")
                        , 2022, 5, 1, 1
                        , eva_toInt("カニちゃん(カニザン)のお化粧備忘録チャンネル"), 3000
                        , eva_toInt("動画内の化粧品まとめ:\n<br>SK-2 税込￥29800\n<br>ニベア 税込￥1980"), eva_toInt("私と同じくらいかわいいですね。")]),

            np.array([150000, 1500, 15000
                        , 1, 10, 300
                        , eva_toInt("じゃんけんの勝ち方、、、徹底解説します。"), eva_toInt("明日から勝率１００パー間違いねぇぜ！")
                        , 2022, 4, 1, 1
                        , eva_toInt("令和のギャンブラー田中一郎の明日から使えるヤバい技チャンネル"), 800
                        , eva_toInt("ネタかと思った。\n<br>でも顔がマジやん。。"), eva_toInt("この動画のおかげで彼女できました！田中一郎に感謝！！。")]),

            np.array([240000, 4800, 30000
                        , 2, 13, 630
                        , eva_toInt("Youtuber、やめます！"), eva_toInt("これで終わりだっ・・。\n<br>今までありがとうございました。")
                        , 2022, 7, 7, 1,
                        eva_toInt("ピカル(Pikaru)"), 180000,
                        eva_toInt("この動画は釣り動画、詐欺動画です。ブラウザバックをお勧めします。"), eva_toInt("ごみ！\n\n<br><br><br><br><br><br><br><br>しね！")]),

    ])

#釣り動画＝1 普通動画＝0 # 2 ＝　ネタ動画
answer_data_y = np.array([0, 0, 0, 1, 1])


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

'''
YOUTUBE_API_KEY = 'AIzaSyCu7OyzTomXx6rujSKQCzS4aSAjgfBFqB8'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def setVideoDatas():

    dayB = datetime.date.fromisoformat('2022-06-01')
    dayB = datetime.datetime.strftime(dayB, '%Y-%m-%dT%H:%M:%S.%fZ')

    dayA = datetime.date.today()
    dayA = datetime.datetime.strftime(dayA, '%Y-%m-%dT%H:%M:%S.%fZ')


    search_response = youtube.search().list(
    part='snippet',
    order='rating',
    type='video',
    regionCode='JP',
    maxResults=50,
    channelId='UCaminwG9MTO4sLYeC3s6udA',
    publishedAfter=dayB,
    publishedBefore=dayA,
    ).execute()


    video_ids = []

    videoCountForAPI = 0
    commentCount = 0

    for item in search_response['items'][:50]:
    
        videoCountForAPI += 1

        title = item['snippet']['title']
        description = item['snippet']['description']

        vidDuration = item['contentDetails']['duration']

        url = 'https://www.youtube.com/watch?v=%s' % item["id"]["videoId"]
        thumbnailUrl1 = item["snippet"]["thumbnails"]["default"]["url"]
        thumbnailUrl2 = item["snippet"]["thumbnails"]["high"]["url"]
        dateUploaded = item["snippet"]["publishedAt"]
        channelName = item["snippet"]["channelTitle"]
        videoId = item['id']['videoId']

        res = youtube.videos().list(id=videoId,part='statistics').execute()
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
        print(videoCountForAPI)
  
        commentCount = 0
        toplevelcomment = "a"
        toplevelcommentauthor = "aa"
        fiftyThLevelcomment = "z"
        fiftyThLevelcommentauthor = "zz"

        for item in response["items"]:

            comment = item["snippet"]["topLevelComment"]

            author = comment["snippet"]["authorDisplayName"]

            if commentCount == 0:
                toplevelcomment = comment
                toplevelcommentauthor = author

            comment_text = comment["snippet"]["textDisplay"]
            if commentCount == 49:
                fiftyThLevelcomment = comment_text
                fiftyThLevelcommentauthor = author

            commentCount += 1

            print("[",author,"]  " , comment_text, "コメ目 → ",commentCount)


        print("\n")

        vidMinutes = re.findall(r'T.*M',vidDuration)
        vidMinutesAfter = vidMinutes[1:-1]
        vidSeconds = re.findall(r'M.*S',vidDuration)
        vidSecondsAfter = vidSeconds[1:-1]
        vidSecondsAfterAll = 60 * vidMinutesAfter + vidSecondsAfter

        vidViewCount = res['items']['statistics']['viewCount']
        vidLikeCount = res['items']['statistics']['likeCount']
        vidDislikeCount = res['items']['statistics']['dislikeCount']
        subscriberCount = 0
        if res['items']['statistics']['hiddenSubscriberCount']:
            subscriberCount = vidViewCount
        else:
            subscriberCount = res['items']['statistics']['subscriberCount']

        test_video_data_x[videoCountForAPI-1] = np.array(vidViewCount, vidLikeCount, vidDislikeCount
                                                        , (vidLikeCount*100)/vidViewCount, 1, (vidDislikeCount*100)/vidViewCount
                                                        , eva_toInt(title), eva_toInt(description)
                                                        , dateUploaded.Year, dateUploaded.Month, dateUploaded.Day, dateUploaded.hour
                                                        , eva_toInt(channelName), subscriberCount
                                                        , eva_toInt(toplevelcomment), eva_toInt(fiftyThLevelcomment)),


setVideoDatas()
print(test_video_data_x)

'''

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

print("(4)【モデルとか、データ定義終わり！】\n")


# モデルを格納するためのフォルダが存在しているか確認。 なければ作る。
if is_file0:
    print("\n(5)folder exists")
else:
    print("\n(5)folder not exists")
    os.makedirs('models/')   

print("\n")


# モデルファイルが存在しているか確認。 なければ作りながらやる。
if is_file:

    model = load_model(path)

    print("\n(6)Load Model\n")

else:
    print("\n(6)Start Making Model\n")

    model = Sequential()

    #入力層作成　ニューロン数32　活性化関数＝ReLU　入力数＝16
    model.add(Dense(32, activation='relu',input_dim =16))
    model.add(Dropout(0.4))

    #隠れ層作成　ニューロン数32　活性化関数＝ReLU　
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.4))

    #出力層作成　ニューロン数(出力数)=1　活性化関数＝softmax
    model.add(Dense(2, activation='softmax'))

    #最適化アルゴリズム　= SGD,損失機関=交差エントロピー、尺度＝精度
    model.compile(optimizer='sgd', loss='categorical_crossentropy',metrics=['accuracy'])

    print(model.summary())


def isint(str):  # 整数値を表しているかどうかを判定
    try:
        int(str, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True

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
def DoStudy():

    global study_times_str
    global study_times_int

    global model

    study_times_str = input("\n\n何回学習する...？ [input number and enter, 数字(整数自然数値)を入力！]: ")
    
    checkIfInt()
    
    study_times_int = int(study_times_str)

    history = model.fit(x_train, y_train, epochs=study_times_int, batch_size=10) #batch_sizeは8(2^3)でもいいかも？

    loss, accuracy = model.evaluate(x_test,y_test)
    print("\n\n誤差: [",loss,"], 精度: [",accuracy, "*100%]")

    print("\n\n現在の予測 x_test: \n", model.predict(x_test[:999]))
    print("\n\n現在の予測 x_train: \n", model.predict(x_train[:9]))
    print("\n\ny_test: \n", y_test[:999])
    print("\n\ny_train: \n", y_train[:9])

    print("\n\nhistory = ", history)


# もう一回学習するかコマンド入力させる関数
def yes_no_input():

    choice = input("\n\nもう一回学習する..？？ [y/N, はい/いいえ]: ").lower()

    if choice in ['y', ' y', 'ye', 'yes', 'はい']:
        return True
    elif choice in ['n', ' n', 'no', 'いいえ']:
        return False


loss, accuracy = model.evaluate(x_test,y_test)
print("\n\n誤差: [",loss,"], 精度: [",accuracy, "*100%]")

print("\n\n現在の予測 x_test: \n", model.predict(x_test[:999]))
print("\n\n現在の予測 x_train: \n", model.predict(x_train[:9]))

print("\n\ny_test: \n", y_test[:999])
print("\n\ny_train: \n", y_train[:9])

DoStudy() # 一回目の学習を行う

# 二回目以降は、選択させる。
while(yes_no_input()):
    DoStudy()


model.save(path) #モデルを保存


print("\n(7)終わりってことだよぉ！(すべての最後―終わり―)\n")

