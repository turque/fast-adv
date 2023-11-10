import logging

import sentry_sdk
from fastapi import FastAPI

from app.routes import auth, invites, races, resources, teams, users
from app.settings import Settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings = Settings()


logger.info('Initialize Sentry SDK')
sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(resources.router)
app.include_router(teams.router)
app.include_router(invites.router)
app.include_router(races.router)


@app.get('/')
async def root():
    return {'status': 'alive'}
