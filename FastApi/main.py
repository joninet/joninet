from fastapi import FastAPI
from routers.product import router as productRouter

app=FastAPI()
app.include_router(productRouter)

@app.get('/')
def message():
    return "hello world"





