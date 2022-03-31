from fastapi import FastAPI
import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from . import models
from .schemas import User,Item
from .database import SessionLocal

app = FastAPI()

@app.get("/")
def index():
    return "Hi"

