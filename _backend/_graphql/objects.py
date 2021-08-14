import graphene
from _database.models import Table as TableModel, Table2 as Table2Model
from graphene_sqlalchemy import SQLAlchemyObjectType

# CUSTOM NODE
class CustomNode(graphene.relay.Node):
    class Meta:
        name = "CustomNode"

    @staticmethod
    def to_global_id(type_, id):
        return id


# OBJECTS
class Table(SQLAlchemyObjectType):
    """returns the Table from the database"""

    class Meta:
        model = TableModel
        interfaces = (CustomNode,)


class Table2(SQLAlchemyObjectType):
    """returns the Table from the database"""

    class Meta:
        model = Table2Model
        interfaces = (CustomNode,)
