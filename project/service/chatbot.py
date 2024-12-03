import openai
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_response(user_input: str) -> str:
    """
    사용자 입력을 ChatGPT API에 전달하고 응답을 반환합니다.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
        )
        # 최신 API에서 응답 가져오기
        return response.choices[0].message["content"]
    except Exception as e:
        return "연결 진행중..."
