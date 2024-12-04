from flask import Flask, request, jsonify
from app.chatbot import chatbot_with_crawling

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    """
    사용자의 질문에 대해 크롤링 데이터 또는 GPT를 통해 응답
    """
    data = request.json
    user_question = data.get("message", "")

    # 챗봇 로직 실행
    answer = chatbot_with_crawling(user_question)

    # 응답 반환
    return jsonify({"response": answer})


if __name__ == "__main__":
    app.run(debug=True)
