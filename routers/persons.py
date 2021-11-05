from uuid import UUID
from typing import List
from fastapi import APIRouter, Depends
from starlette import status
from schemas.persons import PersonSchemaIn, PersonSchemaOut
from db.database.setup import get_db
from repositories.persons import PersonRepository
from sqlalchemy.orm.session import Session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PersonSchemaOut)    
async def create_person(payload: PersonSchemaIn, db: Session=Depends(get_db)) -> PersonSchemaOut:
    person_repository: PersonRepository = PersonRepository(db=db)
    return person_repository.create_item(person=payload)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[PersonSchemaOut])
async def get_all(db: Session=Depends(get_db)) -> List[PersonSchemaOut]:
    return PersonRepository(db=db).get_all();

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=PersonSchemaOut)  
async def get_person(id: UUID, db: Session=Depends(get_db)) -> PersonSchemaOut:
    return PersonRepository(db=db).get_item(id=id) 

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=PersonSchemaOut)     
async def update_person(id: UUID, payload: PersonSchemaIn, db: Session=Depends(get_db)) -> PersonSchemaOut:
    updated_item = PersonRepository(db=db).update_item(id=id, person=payload)
    if updated_item is None:
        return {"message": "Not found"}
        
    return updated_item

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def drop_person(id: UUID, db: Session=Depends(get_db)):
    PersonRepository(db=db).drop_item(id=id)
    return {"message": "person deleted"}
