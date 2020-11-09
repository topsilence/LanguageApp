from flask import Flask,  render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/main")
def move_main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
