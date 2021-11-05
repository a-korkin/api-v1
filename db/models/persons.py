import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey
# from db.database.setup import Base
from db.models.entity import Entity

class Person(Entity):
    __tablename__ = "cd_persons"
    __table_args__ = {"schema": "common", "comment": "физлица"}
    id = Column(UUID(as_uuid=True), ForeignKey("common.cd_entities.id"), primary_key=True, default=uuid.uuid4, comment="идентификатор")
    last_name = Column("c_last_name", String(500), nullable=False, comment="фамилия")
    first_name = Column("c_first_name", String(500), nullable=False, comment="имя")
