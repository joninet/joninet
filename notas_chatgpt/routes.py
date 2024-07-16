from fastapi import APIRouter, Depends, Request, Form
from fastapi.security import HTTPBasicAuth, HTTPBasicScheme
from models import Usuario, Nota
from database import obtener_conexion, verificar_contrasena, crear_usuario, obtener_notas_por_usuario, obtener_nota_por_id, crear_nota, editar_nota, eliminar_nota
from typing import List

router = APIRouter()

auth_scheme = HTTPBasicScheme(security_scheme_name="basic")


@auth_scheme.get_user
async def get_user(username: str, password: str):
    conexion = obtener_conexion()
    usuario = verificar_contrasena(conexion, username, password)
    cerrar_conexion(conexion)
    return usuario


@router.post("/usuario/registro")
async def registrar_usuario(username: str = Form(), password: str = Form()):
    conexion = obtener_conexion()
    crear_usuario(conexion, username, password)
    cerrar_conexion(conexion)
    return {"mensaje": "Usuario registrado exitosamente"}


@router.post("/usuario/login")
async def login_usuario(username: str = Form(), password: str = Form(), request: Request):
    conexion = obtener_conexion()
    usuario = verificar_contrasena(conexion, username, password)
    cerrar_conexion(conexion)
    if usuario is None:
        return {"mensaje": "Usuario o contraseña incorrectos"}

    # Generar token de autenticación (implementar en producción)
    token = "token_de_ejemplo"

    return {"mensaje": "Inicio de sesión exitoso", "token": token}


@router.get("/notas", dependencies=[Depends(get_user)])
async def obtener_todas_las_notas(usuario: Usuario):
    conexion = obtener_conexion()
    notas = obtener_notas_por_usuario(conexion, usuario.id_usuario)
    cerrar_conexion(conexion)
    return notas


@router.get("/notas/{nota_id}", dependencies=[Depends(get_user)])
async def obtener_nota_por_id(nota_id: int, usuario: Usuario):
    conexion = obtener_conexion()
    nota = obtener_nota_por_id
