from js import document 
import random

foods = [
    "エッグマックマフィン", "ベーコンエッグマックサンド", "ソーセージエッグマフィン", "ソーセージマフィン",
    "チキンマックマフィン", "フィレオフィッシュ","ホットケーキ", "マックグリドルソーセージエッグ",
    "マックグリドルベーコンエッグ", "マックグリドルソーセージ", "メガマフィン"
]

mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

def get_random_food():
    return random.choice(foods)

def handle_submit(event):
    event.preventDefault()

    user_input = document.getElementById('mbti').value.upper()
    if user_input in mbti_types:
        food = get_random_food()
        document.getElementById('result').innerHTML = f"おすすめの食べ物: {food}"
    else:
        document.getElementById('result').innerHTML = "MBTIを教えてね"

document.getElementById('mbtiForm').addEventListener('submit', handle_submit)