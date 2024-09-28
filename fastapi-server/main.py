from fastapi import FastAPI
from api import customers
from api.database import engine
from api import models

app = FastAPI()

app.include_router(customers.router)

models.Base.metadata.create_all(bind=engine)


