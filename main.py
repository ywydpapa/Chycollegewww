from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from routers import board


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"
# FastAPI 앱 초기화
app = FastAPI(title="CHY College Homepage")

# 정적 파일(CSS, JS, 이미지 등) 마운트
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.include_router(board.router)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/chymain", response_class=HTMLResponse)
async def chymain(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/chy/mainpage.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/greet", response_class=HTMLResponse)
async def greet(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/chy/greetings.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )

@app.get("/advisors", response_class=HTMLResponse)
async def advisors(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/chy/advisor.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )

@app.get("/map", response_class=HTMLResponse)
async def map(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/chy/tmap.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )

@app.get("/edu_main", response_class=HTMLResponse)
async def edumain(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/edu/edumain.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )

@app.get("/edu_chy", response_class=HTMLResponse)
async def educhy(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/edu/edu_chy.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )

@app.get("/edu_cur", response_class=HTMLResponse)
async def educur(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/edu/edu_cur.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )

@app.get("/edu_teachers", response_class=HTMLResponse)
async def eduteachers(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/edu/edu_teachers.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/gallery", response_class=HTMLResponse)
async def gallery(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/edu/gallery.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/event_main", response_class=HTMLResponse)
async def eventmain(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/event/eventmain.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/event_01", response_class=HTMLResponse)
async def event01(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/event/event01.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/event_02", response_class=HTMLResponse)
async def event02(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/event/event02.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )

@app.get("/event_03", response_class=HTMLResponse)
async def event03(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/event/event03.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/noble_main", response_class=HTMLResponse)
async def noblemain(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/nobl/noble_main.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/noble01", response_class=HTMLResponse)
async def noble01(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/nobl/noble01.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/utb", response_class=HTMLResponse)
async def utb(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/utb.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/jebomain", response_class=HTMLResponse)
async def jebomain(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/jebomain.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )


@app.get("/jebo01", response_class=HTMLResponse)
async def jebo01(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="/jebo01.html",
        context={
            "title": "CHYC - 사단법인 충효예대학",
        },
    )