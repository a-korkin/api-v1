from sqlalchemy.orm.session import Session
from schemas.persons import PersonSchemaIn, PersonSchemaOut
from db.models.persons import Person

class PersonRepository():
    def __init__(self, db: Session):
        self.db = db

    def create_item(self, in_person: PersonSchemaIn) -> PersonSchemaOut:
        item = Person()
        item.last_name = in_person.last_name
        item.first_name = in_person.first_name
        self.db.add(item)        
        self.db.commit()
        self.db.refresh(item)
        return PersonSchemaOut.from_orm(item)
