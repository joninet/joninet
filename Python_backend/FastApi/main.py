from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI"
#uvicorn main:app --reload       / main(nombre del fichero que queremos arrancar), app(instancia de fast api), reload(recarga el contecto cada vez que hsy cambios )
