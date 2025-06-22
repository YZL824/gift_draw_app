from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 礼物列表
gifts = ["香水", "手表", "书籍《活着为了什么》", "一次浪漫旅行", "手写情书", "定制首饰"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/draw")
def draw():
    gift = random.choice(gifts)
    return jsonify({"gift": gift})

# 新增通配路由（关键！捕获所有未定义的路径）
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  # 确保生产环境可访问
