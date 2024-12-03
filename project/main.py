from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

# 설정된 HTML 템플릿 경로
TEMPLATES_DIR = Path(__file__).parent / "templates"

# 기본 엔드포인트
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(TEMPLATES_DIR / "index.html", "r", encoding="utf-8") as file:  # 인코딩 명시
        html_content = file.read()
    return html_content
