from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse
import os

app = FastAPI()

path = os.getcwd()


@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


@app.get("/api/img/{filename}")
def get_img(filename: str):
    filepath = os.path.join(f"{path}/public/img/", os.path.basename(filename))
    return FileResponse(filepath)


@app.post("/api/login")
async def login(request: Request):
    print(request)
    return {"message": "Logado!"}


@app.get("/api/auth/login")
async def read_item(request: Request):
    print(dict(request))
    return {
        "user": {
            "id": 1,
            "username": "arnaldo@turque.com.br",
            "email": "arnaldo@turque.com.br",
            "fullname": "Arnaldo Turque",
            "role": "SUPER",
            "createdAt": "2021-05-30T06:45:19.000Z",
            "name": "Arnaldo Turque",
            "avatar": "/img/perfil-roxo.png"
        },
        "token": "ey...",
    }
