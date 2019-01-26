import graphene
from starlette.graphql import GraphQLApp as BaseGraphQLApp
from starlette.responses import HTMLResponse

from ..playground import PLAYGROUND


class GraphQLApp(BaseGraphQLApp):
    async def handle_graphiql(self, request):
        return HTMLResponse(PLAYGROUND)
