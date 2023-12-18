from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
#OAuth2PasswordBearer: se encarga de gestionar la autenticacion(usuario y contraseña)
#OAuth2PasswordRequestForm: es la forma en la que se va enviar estos criterios de autentificacion a nuestra API

app = FastAPI()

oauth2=OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    fullName: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

usersDb = {
    "joninet": {
        "username": "joninet",
        "fullName": "jonathan Desplats",
        "email": "joninet2971@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "joninet2": {
        "username": "joninet2",
        "fullName": "jonathan Desplats 2",
        "email": "joninet29712@gmail.com",
        "disabled": True,
        "password": "123456"
    }
}

def searchUser(username: str):
    if username in usersDb:
        return UserDB(usersDb[username])
    
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    usersDb = usersDb.get(form.username)
    if not usersDb:
        raise HTTPException(status_code=400, detail="el usuario ya existe")
    user= searchUser(form.username)
    if not form.username == user.password:
        raise HTTPException(status_code=400, detail="la contraseña no es correcta")
    
    return {"access_token": user.username, "token_type": "bearer"}
