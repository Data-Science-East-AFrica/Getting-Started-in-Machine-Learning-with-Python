from models import db
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
db.init_app(app)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def Index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/blogs/{id}")
async def blogs(id:int):
	return {'data':id} 


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
                                                                @Lux_Academy🐦
