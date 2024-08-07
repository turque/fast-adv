from fastapi import APIRouter

from .endpoints import (
    athlete,
    auth,
    invites,
    races,
    resources,
    strategic_planning,
    teams,
    utils,
)

api_router = APIRouter()
api_router.include_router(
    athlete.router, prefix='/athletes', tags=['athletes']
)
api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(resources.router)
api_router.include_router(teams.router, prefix='/teams', tags=['teams'])
api_router.include_router(invites.router, prefix='/invite', tags=['invites'])
api_router.include_router(races.router, prefix='/races', tags=['races'])
api_router.include_router(utils.router, prefix='/utils', tags=['utils'])
api_router.include_router(
    strategic_planning.router, prefix='/strategic', tags=['strategic planning']
)
