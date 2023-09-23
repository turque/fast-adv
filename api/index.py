from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

path = os.getcwd()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/img/{filename}")
def get_img(filename: str):
    filepath = os.path.join(f'{path}/public/img/', os.path.basename(filename))
    return FileResponse(filepath)