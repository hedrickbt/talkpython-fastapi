import json
from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/')
def index():
    body = """
    <html>
    <body style='padding: 10px;'>
    <h1>Welcome to the API</h1>
    <div>
    Try it: <a href='/api/calculate/?x=7&y=11'>/api/calculate/?x=7&y=11</a>
    </div>
    </body>
    </html>
"""
    return fastapi.responses.HTMLResponse(content=body)


@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        error = {
            'error': 'ERROR: z cannot be 0.'
        }
        # return fastapi.Response(content=json.dumps(error), media_type='application/json', status_code=400)
        return fastapi.responses.JSONResponse(content=error, status_code=400)

    value = (x + y)
    if z is not None:
        value /= z
    return {
        'x': x,
        'y': y,
        'z': z,
        'value': value,
    }


uvicorn.run(api, port=8001, host='127.0.0.1')
