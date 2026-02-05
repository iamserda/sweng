from flask import Flask

app = Flask(__name__)


@app.route("/")
def handle_home():
    return "<h1>Hello Flask App World!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8882", debug=True)
