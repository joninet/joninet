from fastapi import FastAPI
from routers.productos import router as productoRouter

app=FastAPI()
app.include_router(productoRouter)

@app.get('/')
def message():
    return "APP de Stock"