from flask import Flask, render_template, request
import random

app = Flask(__name__)

foods = [
  "エッグマックマフィン", "ベーコンエッグマックサンド", "ソーセージエッグマフィン", "ソーセージマフィン", "チキンマックマフィン", "フィレオフィッシュ",
  "ホットケーキ", "マックグリドルソーセージエッグ", "マックグリドルベーコンエッグ", "マックグリドルソーセージ", "メガマフィン"
]

mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('mbti').upper()
        if user_input in mbti_types:
            food = random.choice(foods)
            result = f"{food}"
        else:
            result = "MBTIを教えてね"
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
