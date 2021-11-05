from fastapi import APIRouter, Depends
from starlette import status
from schemas.persons import PersonSchemaIn, PersonSchemaOut
from db.database.setup import get_db
from repositories.persons import PersonRepository
from sqlalchemy.orm.session import Session

router = APIRouter()

@router.get("/")
async def index():
    return {"hello": "world"}

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PersonSchemaOut)    
async def create_person(payload: PersonSchemaIn, db_item: Session = Depends(get_db)) -> PersonSchemaOut:
    person_repository: PersonRepository = PersonRepository(db=db_item)
    return person_repository.create_item(in_person=payload)
