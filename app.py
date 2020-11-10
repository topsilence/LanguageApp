import os
# splite3をimportする
import sqlite3
# flaskをimportしてflaskを使えるようにする
from flask import Flask , render_template , request , redirect
# appにFlaskを定義して使えるようにしています。Flask クラスのインスタンスを作って、 app という変数に代入しています。
app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabakoza'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/test")
def scene_1():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_infos = c.fetchall
    for row in c.execute('SELECT english, japanese, pronunciation from greetings ORDER BY id'):
        print(str(row[0]), row[1], row[2])
    c.close()
    return render_template("test.html", word_info = row)

@app.route("/scene_2")
def scene_2():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    c.execute("SELECT english, japanese, pronunciation FROM shopping WHERE id = 1")
    # 取ってきた内容を変数に格納する
    word_info = c.fetchone()
    # データベースの接続終了
    c.close()
    return render_template("scene_2.html", word_info=word_info)

@app.route("/scene_3")
def scene_3():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    c.execute("SELECT english, japanese, pronunciation FROM eatingout WHERE id = 1")
    # 取ってきた内容を変数に格納する
    word_info = c.fetchone()
    # データベースの接続終了
    c.close()
    return render_template("scene_3.html", word_info=word_info)

@app.route("/scene_4")
def scene_4():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    c.execute("SELECT english, japanese, pronunciation FROM directions WHERE id = 1")
    # 取ってきた内容を変数に格納する
    word_info = c.fetchone()
    # データベースの接続終了
    c.close()
    return render_template("scene_4.html", word_info=word_info)

@app.route("/scene_5")
def scene_():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    c.execute("SELECT english, japanese, pronunciation FROM conversation WHERE id = 1")
    # 取ってきた内容を変数に格納する
    word_info = c.fetchone()
    # データベースの接続終了
    c.close()
    return render_template("scene_5.html", word_info=word_info)

@app.route("/scene_6")
def scene_6():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    c.execute("SELECT english, japanese, pronunciation FROM emagency_sick WHERE id = 1")
    # 取ってきた内容を変数に格納する
    word_info = c.fetchone()
    # データベースの接続終了
    c.close()
    return render_template("scene_6.html", word_info=word_info)

@app.route("/scene_7")
def scene_7():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    c.execute("SELECT english, japanese, pronunciation FROM numbers WHERE id = 1")
    # 取ってきた内容を変数に格納する
    word_info = c.fetchone()
    # データベースの接続終了
    c.close()
    return render_template("scene_7.html", word_info=word_info)

@app.route("/scene_8")
def scene_8():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    c.execute("SELECT english, japanese, pronunciation FROM time_date WHERE id = 1")
    # 取ってきた内容を変数に格納する
    word_info = c.fetchone()
    # データベースの接続終了
    c.close()
    return render_template("scene_8.html", word_info=word_info)

@app.route("/scene_9")
def scene_9():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    c.execute("SELECT english, japanese, pronunciation FROM dating WHERE id = 1")
    # 取ってきた内容を変数に格納する
    word_info = c.fetchone()
    # データベースの接続終了
    c.close()
    return render_template("scene_9.html", word_info=word_info)

@app.errorhandler(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@app.errorhandler(404)
def notfound404(code):
    return "404だよ！！見つからないよ！！！"


# __name__ というのは、自動的に定義される変数で、現在のファイル(モジュール)名が入ります。 ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)