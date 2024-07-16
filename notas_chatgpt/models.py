from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(255), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)

    notas = relationship("Nota", backref="usuario")


class Nota(Base):
    __tablename__ = "notas"

    id_nota = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    contenido = Column(String(text), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)

    usuario = relationship("Usuario", backref="notas")
