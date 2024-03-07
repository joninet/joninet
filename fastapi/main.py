from fastapi import FastAPI
from productos import router as router_prod

app = FastAPI()

app.include_router(router_prod)
