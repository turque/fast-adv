from fastapi import FastAPI

from api.routes import auth, invites, resources, teams, users, races

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(resources.router)
app.include_router(teams.router)
app.include_router(invites.router)
app.include_router(races.router)


@app.get('/')
async def root():
    return {'message': 'Hello, wellcome to Fast ADV API!'}
