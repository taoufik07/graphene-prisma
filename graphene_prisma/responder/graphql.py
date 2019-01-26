import graphene
from responder.ext import GraphQLView as BaseGraphQLView

from ..playground import PLAYGROUND


class GraphQLView(BaseGraphQLView):
    async def graphql_response(self, req, resp, schema):
        if req.method not in ("get", "post", "head"):
            resp.status_code = 405

        if req.method in ("get", "head") and req.accepts("text/html"):
            resp.content = self.api.template_string(PLAYGROUND, endpoint=req.url.path)
            return

        return await super().graphql_response(req, resp, schema)
