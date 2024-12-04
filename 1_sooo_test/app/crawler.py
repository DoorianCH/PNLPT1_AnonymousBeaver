import json


def get_crawling_data():
    """
    크롤링 데이터를 JSON 파일에서 읽어오는 함수
    """
    with open("data/crawling_data.json", "r", encoding="utf-8") as f:
        return json.load(f)
