#203213ゆゆゆ

#203211noog

#203105かにかに

#203128bit

#203210れお

#*******************************************************



#tkinterのインポート
import tkinter

from tkinter import Text, Tk, ttk

#tkinterを起動
root = tkinter.Tk()

#タイトルの設定
root.title("釣り動画判別ソフト : メインメニュー")

#画面サイズの指定
root.geometry("1000x500")

def close_window():
    root.destroy()

"""
def cry_window():
    root.destroy()
"""

# ラベル表示
label_title = tkinter.Label(root, text="Youtube 釣り動画判別", font=("MSゴシック", "20", "bold"))
label_title.grid()

label_desc = tkinter.Label(root, text="(選択肢ボタン)\n(URL検索)\nor(チャンネルID検索)", font=("MSゴシック", "12", "bold"))
label_desc.grid()

label_inputURL = tkinter.Label(root, text="URLを入力↓", font=("MSゴシック", "12", "bold"))
label_inputURL.grid()

"""
label_tikawa = tkinter.Label(root, text="ワ・・・ツール", font=("MSゴシック", "20", "bold"))
label_tikawa.grid()
"""

# ボタンの設定(text=ボタンに表示するテキスト)
btn_go = tkinter.Button(root, text='Go',
width = 10,
height = 3,
foreground = "Black",
bg = "Cyan",
)

text_input = tkinter.Text(root, 
width = 85,
height = 3,
pady = 3,
wrap = tkinter.NONE,
foreground = "Black",
bg = "Cyan",
)

"""
btn_close = tkinter.Button(root, text='閉じる',
width = 20,
height = 2,
bg = "White",
command = close_window
)
"""

#ボタンやテキストを配置する位置の設定

label_title.place(x=350, y=50)

label_desc.place(x=410, y=115)

label_inputURL.place(x=440, y=200)

text_input.place(x=210, y=255)
#text_input.insert(0, "https://www.youtube.com/watch?v=5qWYfTlAJsg")

btn_go.place(x=450, y=325)

#btn_close.place(x=700, y=450)


"""
btn1 = tkinter.Button(root, text='チャンネルID検索',
width = 50,
height = 2,
bg = "White",
)

btn2 = tkinter.Button(root, text='ちいかわ',
width = 50,
height = 2,
bg = "White",
)

btn3 = tkinter.Button(root, text='泣いちゃった',
width = 50,
height = 2,
bg = "White",
command = cry_window
)

#btn1.place(x=20, y=120)

#btn2.place(x=20, y=180)

#btn3.place(x=20, y=240)
"""


root.mainloop()