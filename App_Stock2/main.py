from fastapi import FastAPI
from routers.product import router as productRouter
from routers.entry_product import router as entryProductRouter


app=FastAPI()
app.include_router(productRouter)
app.include_router(entryProductRouter)


@app.get('/')
def message():
    return "APP de Stock"