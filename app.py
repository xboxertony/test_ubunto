from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "ubunto 測試成功!!!!!!"

if __name__=="__main__":
    app.run(debug=True)