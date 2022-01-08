import json
from pathlib import Path

import fastapi
import sentry_sdk
import uvicorn
from starlette.staticfiles import StaticFiles
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from api import weather_api
from services import openweather_service
from views import home

sentry_sdk.init(
    "https://0da645162ce949209202a08e9873a4c2@o1110945.ingest.sentry.io/6140069",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

api = fastapi.FastAPI()
api.add_middleware(SentryAsgiMiddleware)


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f'WARNING: {file} file not found, you cannot continue, please see settings_template.json')
        raise Exception('settings.json file not found, you cannot continue, please see settings_template.json')
    with open('settings.json') as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get('api_key')


def configure():
    configure_routing()
    configure_api_keys()


if __name__ == '__main__':
    # local development
    configure()
    uvicorn.run(api, port=8001)
else:
    # production
    configure()