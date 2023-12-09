from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

usersList = [User(id=1, name="Braiss", surname="Moure", url="https://moure.dev", age=35),
            User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
            User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)]

@app.get("/users")
async def users():
    return usersList

#Path

@app.get("/user/{id}")
async def user(id: int):
# La función filter() filtra elementos de una secuencia (en este caso, una lista) basándose en una función de filtro.
# La función lambda aquí se utiliza para definir una función pequeña (anónima) que verifica si el id de un usuario es igual al id proporcionado.
    """users = filter(lambda user: user.id == id, usersList)
    try:
        return list(users)[0]
    except:
        return {"error":"no se encontro el usuario"}"""
    return searchUser(id)
    
@app.get("/users")
async def users():
    return usersList


#query
#http://127.0.0.1:8000/userQuery/?id=1

@app.get("/user/")
async def user(id: int):
    return searchUser(id)
    
def searchUser(id:int):
    users = filter(lambda user: user.id == id, usersList)
    try:
        return list(users)[0]
    except:
        return {"error":"no se encontro el usuario"}