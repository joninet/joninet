from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#uvicorn users:app --reload

router= APIRouter()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

usersList = [User(id=1, name="Braiss", surname="Moure", url="https://moure.dev", age=35),
            User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
            User(id=3, name="Brais", surname="Dahlberg", url="https://haakon.com", age=33)]

@router.get("/users")
async def users():
    return usersList

#Path

@router.get("/user/{id}")
async def user(id: int):
# La función filter() filtra elementos de una secuencia (en este caso, una lista) basándose en una función de filtro.
# La función lambda aquí se utiliza para definir una función pequeña (anónima) que verifica si el id de un usuario es igual al id proporcionado.
    """users = filter(lambda user: user.id == id, usersList)
    try:
        return list(users)[0]
    except:
        return {"error":"no se encontro el usuario"}"""
    return searchUser(id)
    
@router.get("/users")
async def users():
    return usersList


#query
#http://127.0.0.1:8000/userQuery/?id=1

@router.get("/user/")
async def user(id: int):
    return searchUser(id)

#creamos usuario
@router.post("/user/", response_model= User, status_code= 201)
async def user(user: User):
    if type(searchUser(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        usersList.append(user)
        return user

#editamos usuario
@router.put("/user/")
async def user(user: User):
    encontro=False
    for index, searchUser in enumerate(usersList):
        if searchUser.id == user.id:
            usersList[index]=user
            encontro=True
    if not encontro:
        return {"error":"no se encontro el usuario"}
    else:
        return user
    
#eliminamos usuario
@router.delete("/user/{id}")
async def user(id: int):
    encontro=False
    for index, searchUser in enumerate(usersList):
        if searchUser.id == id:
            del usersList[index]
            encontro = True
    if not encontro:
        return {"Error": "No se elimino el usuario"}



def searchUser(id:int):
    users = filter(lambda user: user.id == id, usersList)
    try:
        return list(users)[0]
    except:
        return {"error":"no se encontro el usuario"}