from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users = [User()]

@app.get('/usersjson')
async def usersjson():
    return [{"name": "Jonathan", "surname": "Desplats", "url": "https://moure.dev", "age": 23},
            {"name": "Jonathan2", "surname": "Desplats2", "url": "https://moure.dev", "age": 23},
            {"name": "Jonathan3", "surname": "Desplats3", "url": "https://moure.dev", "age": 23}]