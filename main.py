# uvicorn main:app --reload --host=0.0.0.0 --port=8000

from fastapi import FastAPI, Header
import models.get_api as get

app = FastAPI()


@app.get("/where/")
async def samsung(station: str = Header(), direction: str = Header()):
    response = get.request_api(station)
    filtered_data = get.data_filter(response, direction)

    return filtered_data
