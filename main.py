import aioredis

from contextlib import asynccontextmanager
from fastapi import FastAPI

from src import models, fake_db

###################### REDIS

redis: aioredis.Redis | None = None

async def connect_to_redis() -> None:
    global redis
    redis = aioredis.Redis(host = "localhost", port = 6379, db=0)

###################### POSTGRESQL

postgresql: None = None

async def connect_to_postgresql() -> None:
    global postgresql
    postgresql = None


db: dict = fake_db.fake_db

###################### API

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_redis()
    await connect_to_postgresql()

    yield

    if redis is not None:
        await redis.close()
    if postgresql is not None:
        pass

app = FastAPI(lifespan = lifespan)

@app.get('/')
async def root() -> dict:
    response = {"root" : "hola puta xddddd"}
    return response

@app.get('/get_entry/id={id}')
async def get_entry(id: int) -> models.Entry:
    entry_name = await redis.get(id)
    entry = models.Entry(id=id, name = entry_name)
    return entry

@app.post('/post_entry/')
async def post_entry(entry: models.Entry) -> models.Entry:
    name = entry.id
    value = entry.name
    await redis.set(name = name, value = value)
    return entry

@app.put('/put_entry/id={id}')
async def put_entry(id: int, entry: models.Entry) -> models.Entry:
    entry.id = id
    return entry

@app.delete('/delete_entry/id={id}')
async def delete_entry(id: int) -> models.Entry:
    entry = models.Entry(id=id)
    return entry