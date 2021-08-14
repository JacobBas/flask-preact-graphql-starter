import graphene
from _backend.graphql.objects import Table, Table2
from typing import Union


class QueryTable(graphene.ObjectType):
    table = graphene.List(
        Table, id=graphene.Argument(type=graphene.Int, required=False)
    )

    @staticmethod
    def resolve_table(
        args,
        info,
        id: Union[int, None] = None,
        boolean: Union[bool, None] = None,
    ):

        # initialize the query
        query = Table.get_query(info)

        # applying filters
        if id:
            query = query.filter(Table._meta.model.id == id)

        if boolean:
            query = query.filter(Table._meta.model.boolean == boolean)

            # returning the queried data
        return query.all()


class QueryTable2(graphene.ObjectType):
    table2 = graphene.List(
        Table2, id=graphene.Argument(type=graphene.Int, required=False)
    )

    @staticmethod
    def resolve_table(
        args,
        info,
        id: Union[int, None] = None,
    ):

        # initialize the query
        query = Table2.get_query(info)

        # applying filters
        if id:
            query = query.filter(Table2._meta.model.id == id)

            # returning the queried data
        return query.all()


class Query(QueryTable, QueryTable2):
    node = graphene.relay.Node.Field()
