import os
# splite3をimportする
import sqlite3
# flaskをimportしてflaskを使えるようにする
from flask import Flask, render_template, request, redirect
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


@app.route("/scene_1")
def scene_1():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from greetings ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_1.html", html_word_info=word_info)


@app.route("/scene_2")
def scene_2():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from shopping ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_2.html", html_word_info=word_info)


@app.route("/scene_3")
def scene_3():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from eatingout ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_3.html", html_word_info=word_info)


@app.route("/scene_4")
def scene_4():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from directions ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_4.html", html_word_info=word_info)


@app.route("/scene_5")
def scene_():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from conversation ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_5.html", html_word_info=word_info)


@app.route("/scene_6")
def scene_6():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from emergency_sick ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_6.html", html_word_info=word_info)


@app.route("/scene_7")
def scene_7():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute('SELECT id, english, japanese, pronunciation from numbers ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_7.html", html_word_info=word_info)


@app.route("/scene_8")
def scene_8():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from time_date ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_8.html", html_word_info=word_info)


@app.route("/scene_9")
def scene_9():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute('SELECT id, english, japanese, pronunciation from dating ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_9.html", html_word_info=word_info)


@app.errorhandler(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@app.errorhandler(404)
def notfound404(code):
    return "404だよ！！見つからないよ！！！"


# __name__ というのは、自動的に定義される変数で、現在のファイル(モジュール)名が入ります。 ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run()
