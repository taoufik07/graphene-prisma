
# Graphene prisma
![License:BSD-3-Clause](https://img.shields.io/github/license/taoufik07/graphene-prisma.svg)
<p align="center">
	<img src="https://i.imgur.com/oLH7R6v.png" alt='prisma playground'>
</p>

Brings prisma playground to graphene and more !

## Install

To install `graphene_prisma`, you need to specify one of the supported frameworks

```python
pip install graphene_prisma
```
or

```python
pip install graphene_prisma[framework]
```

**Supported frameworks :**

- [responder](https://github.com/kennethreitz/responder)
- [starlette](https://github.com/encode/starlette)

**e.g. starlette**

```python
pip install graphene_prisma[starlette]
```

## Usage

To use `graphene_prisma`

```python
from graphene_prisma.[framework] import [GraphQLHandler]
```
- **[framework]** : name of the framework (responder, starlette,...)
- **[GraphQLHandler]**: name of the graphql view in your framework (`GraphQLView` for `responder` and `GraphQLApp` for `starlette` ) 

Here is a list of the corresponding graphql classes to each framework :
<p align="center">

| framework   |  GraphQL view   |
|-------------|-----------------|
|[responder](https://github.com/kennethreitz/responder)| GraphQLView |
|[starlette](https://github.com/encode/starlette)  | GraphQLApp |

</p>

### Starlette

```python
from starlette.applications import Starlette
from graphene_prisma.starlette import GraphQLApp

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return f"Hello {name}"

app = Starlette()
app.add_route('/', GraphQLApp(schema=graphene.Schema(query=Query)))
```

### Responder

```python
import responder
from graphene_prisma.responder import GraphQLView

api = responder.API()

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return f"Hello {name}"

schema = graphene.Schema(query=Query)
view = GraphQLView(api=api, schema=schema)

api.add_route("/graph", view)
api.run()
```

## TODO
* Support other frameworks (django, flask,...)
* Tests
* Upload
