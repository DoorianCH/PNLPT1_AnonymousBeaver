from openai import OpenAI

# OpenAI 클라이언트 초기화
client = OpenAI(api_key="your-secret-key")

GPT_MODEL = "gpt-4o-mini"  # 사용할 모델 이름


def ask_gpt(question):
    """
    GPT에게 질문을 전달하고 응답을 받는 함수
    """
    try:
        # 메시지 구성
        messages = [
            {"role": "system", "content": "You answer questions about Web services."},
            {"role": "user", "content": question},
        ]

        # OpenAI ChatCompletion API 호출
        response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=messages,
            temperature=0,  # 결과의 결정성을 높이기 위해 설정
        )

        # 응답 데이터에서 메시지 추출
        response_message = response.choices[0].message.content
        return response_message

    except Exception as e:
        # API 호출 중 발생한 일반적인 예외 처리
        return f"GPT 호출 중 오류가 발생했습니다: {str(e)}"


def search_in_crawling_data(question):
    """
    크롤링된 데이터에서 질문에 맞는 응답을 찾는 함수
    """
    from app.crawler import get_crawling_data  # 로컬 크롤러에서 데이터 가져오기

    data = get_crawling_data()
    for entry in data:
        if entry["key"] in question:
            return entry["value"]
    return None


def chatbot_with_crawling(user_question):
    """
    사용자 질문 처리: 크롤링 데이터 -> GPT 순으로 응답 생성
    """
    # Step 1: 크롤링 데이터에서 답변 검색
    answer = search_in_crawling_data(user_question)

    # Step 2: 크롤링 데이터에 없으면 GPT에게 질문
    if not answer:
        answer = ask_gpt(user_question)

    return answer
