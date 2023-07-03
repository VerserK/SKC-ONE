from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get('/')
def index():
    hello = 'Hello World!'
    print('Request for index page received')
    return hello

if __name__ == '__main__':
    app.run()

