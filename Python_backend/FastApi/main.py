# Clase en vídeo: https://youtu.be/_y9qQZXE24A

### Hola Mundo ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI

app=FastAPI()

# Url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}
#uvicorn main:app --reload       / main(nombre del fichero que queremos arrancar), app(instancia de fast api), reload(recarga el contecto cada vez que hsy cambios )
