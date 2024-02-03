from fastapi import FastAPI
from routers.product import router as productRouter
from routers.entry_product import routerEntry as entry_productRouter

app=FastAPI()
app.include_router(productRouter)
app.include_router(entry_productRouter)

@app.get('/')
def message():
    return "APP de Stock"