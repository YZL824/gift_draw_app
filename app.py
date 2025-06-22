from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 礼物列表
gifts = ["小米耳机*1", "自选化妆品*1", "自选服装*1"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/draw")
def draw():
    gift = random.choice(gifts)
    return jsonify({"gift": gift})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  # 确保 host 是 0.0.0.0
