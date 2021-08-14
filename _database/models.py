from sqlalchemy import Column, Integer, String, Boolean, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from _database import Base
from typing import Union


class Table(Base):
    """Example table"""

    # META DATA
    __tablename__ = "table"
    __table_args__ = (UniqueConstraint("string", "boolean", name="_string_boolean_uc"),)

    # COLUMNS
    id = Column(Integer, primary_key=True)
    string = Column(String, nullable=False)
    boolean = Column(Boolean, nullable=False)
    date = Column(Date)

    # METHODS
    def __init__(
        self,
        string: Union[str, None] = None,
        boolean: Union[str, None] = None,
        date: Union[str, None] = None,
    ):
        self.string = string
        self.boolean = boolean
        self.date = date


class Table2(Base):
    """Second example table"""

    # META DATA
    __tablename__ = "table2"

    # COLUMNS
    id = Column(Integer, primary_key=True)
    foreign_id = Column(Integer, ForeignKey("table.id"))

    # REALATIONSHIPS
    table = relationship("Table", foreign_keys=[foreign_id])

    # METHODS
    def __init__(
        self,
        foreign_id: Union[int, None] = None,
    ):
        self.foreign_id = foreign_id
