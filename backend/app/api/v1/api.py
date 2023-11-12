from fastapi import APIRouter

from .endpoints import auth, invites, races, resources, teams, users

api_router = APIRouter()
api_router.include_router(
    users.router,
)
api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(resources.router)
api_router.include_router(teams.router)
api_router.include_router(invites.router, prefix='/invite', tags=['invites'])
api_router.include_router(races.router, prefix='/races', tags=['races'])
