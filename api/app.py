from fastapi import FastAPI

from api.routes import auth, resources, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(resources.router)
