from fastapi import FastAPI

from api.routes import auth, invite, resources, teams, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(resources.router)
app.include_router(teams.router)
app.include_router(invite.router)


@app.get('/')
async def root():
    return {'message': 'Hello, wellcome to Fast ADV API!'}
