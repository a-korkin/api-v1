from fastapi import APIRouter
from routers import persons

api_router = APIRouter()
api_router.include_router(persons.router, prefix="/persons")
