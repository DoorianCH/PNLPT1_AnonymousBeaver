from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from service.chatbot import get_chat_response

app = FastAPI()

# HTML 템플릿 디렉토리 설정
TEMPLATES_DIR = Path(__file__).parent / "templates"

# 기본 페이지
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(TEMPLATES_DIR / "index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content

# 챗봇 페이지
@app.get("/chatbot", response_class=HTMLResponse)
async def chatbot_page():
    with open(TEMPLATES_DIR / "chatbot.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content

# 챗봇 응답 API
@app.post("/chatbot-response", response_class=HTMLResponse)
async def chatbot_response(user_input: str = Form(...)):
    response = get_chat_response(user_input)
    return response
