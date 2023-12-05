from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Users():
    name= str
    surname= str
    url= str
    age= int


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Jonathan", "surname": "Desplats", "url": "http://www.joninet.com", "age": 36},
            {"name": "Jon", "surname": "gggg", "url": "http://www.joninet25.com", "age": 30},
            {"name": "Joan", "surname": "Desñp", "url": "http://www.j5454oninet.com", "age": 26}]