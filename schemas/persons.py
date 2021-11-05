from uuid import UUID
from schemas.base import BaseSchema

class PersonSchemaBase(BaseSchema):
    last_name: str
    first_name: str

class PersonSchemaIn(PersonSchemaBase):
    ...

class PersonSchemaOut(PersonSchemaBase):
    id: UUID
