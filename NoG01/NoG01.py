#203213ゆゆゆ
#203211noog
#203105かにかに

#tkinterのインポート
import tkinter

#tkinterを起動
root = tkinter.Tk()
#タイトルの設定
root.title("メインメニュー")
#画面サイズの指定
root.geometry("500x500")

def close_window():
    root.destroy()

# ラベル表示
label = tkinter.Label(root, text="xxxx ツール", font=("MSゴシック", "20", "bold"))
label.grid()

# ボタンの設定(text=ボタンに表示するテキスト)
btn0 = tkinter.Button(root, text='XXXXXX1',
width = 50,
height = 2,
bg = "White",
)
btn1 = tkinter.Button(root, text='XXXXXX2',
width = 50,
height = 2,
bg = "White",
)
btn2 = tkinter.Button(root, text='XXXXXX3',
width = 50,
height = 2,
bg = "White",
)
btn3 = tkinter.Button(root, text='XXXXXX4',
width = 50,
height = 2,
bg = "White",
)
btn_close = tkinter.Button(root, text='閉じる',
width = 20,
height = 2,
bg = "White",
command = close_window
)
#ボタンを配置する位置の設定
btn0.place(x=20, y=60)
btn1.place(x=20, y=120)
btn2.place(x=20, y=180)
btn3.place(x=20, y=240)
btn_close.place(x=325, y=450)

root.mainloop()