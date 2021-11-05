from typing import List
from uuid import UUID
from sqlalchemy.orm.session import Session
from schemas.persons import PersonSchemaIn, PersonSchemaOut
from db.models.persons import Person

class PersonRepository():
    def __init__(self, db: Session):
        self.db = db

    def create_item(self, person: PersonSchemaIn) -> PersonSchemaOut:
        item = Person(**person.dict())
        self.db.add(item)        
        self.db.commit()
        self.db.refresh(item)
        return PersonSchemaOut.from_orm(item)

    def get_all(self) -> List[PersonSchemaOut]:       
        return self.db.query(Person).order_by(Person.last_name.desc()).all()

    def get_item(self, id: UUID) -> PersonSchemaOut:
        return self.db.query(Person).filter_by(id=id).first()

    def update_item(self, id: UUID, person: PersonSchemaIn) -> PersonSchemaOut:
        item = self.db.query(Person).filter_by(id=id).first()

        if item is not None:
            item.last_name = person.last_name
            item.first_name = person.first_name
            self.db.commit()
            self.db.refresh(item)

            return PersonSchemaOut.from_orm(item)
        
        return None
            
    def drop_item(self, id: UUID):
        person = self.db.query(Person).filter_by(id=id).first()
        self.db.delete(person)
        self.db.commit()
