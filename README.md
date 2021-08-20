# Iris dataset on GraphQL
This is an implementation of graphql in python.

## Intro

![image](https://user-images.githubusercontent.com/50926437/130272807-b37f02dc-4f56-4d63-ba34-f6bb27925c96.png)

GraphQL is a query language and server-side runtime for application programming interfaces (APIs) that prioritizes giving clients exactly the data they request and no more. 

GraphQL is designed to make APIs fast, flexible, and developer-friendly. It can even be deployed within an integrated development environment (IDE) known as GraphiQL. As an alternative to REST, GraphQL lets developers construct requests that pull data from multiple data sources in a single API call. 

Additionally, GraphQL gives API maintainers the flexibility to add or deprecate fields without impacting existing queries. Developers can build APIs with whatever methods they prefer, and the GraphQL specification will ensure they function in predictable ways to clients.

API developers use GraphQL to create a schema to describe all the possible data that clients can query through that service. 

A GraphQL schema is made up of object types, which define which kind of object you can request and what fields it has. 

As queries come in, GraphQL validates the queries against the schema. GraphQL then executes the validated queries.

The API developer attaches each field in a schema to a function called a resolver. During execution, the resolver is called to produce the value.

## Why graphql over REST?
* Standard: No fightinh over what is the right way to do REST. The spec is defined.
* Development environment
* Get exactly what you want
* Types
* Lower Network Overhead
* No Versioning: It is append only, you don't have to painful versions

## What does python have to offer for GraphQL?

![image](https://user-images.githubusercontent.com/50926437/130273461-a90001a1-d28f-46e7-be0d-d6523a0d6f81.png)

We have `GRAPHENE` for that.

### What is GRAPHINE?
* Graphql implementation for Python
* Is very popular
  * 2nd only to FB implementation
* Has many production users
  * Yelp, mozilla
* Integrations with popular frameworks
  * Django, Flask, Pyramid
* Integrations with popular ORMs
  * Django, SQLAlchemy, Peewee, GAE

### Terminology
* Type/Objects: Sort of like seralizers for graphql
* Schema: The container of all the graphql types at your disposal
* Resolver: The function that is executed to give back the data for a single attribute of a type/object
* Query: What you use to get or set data using graphql
* Mutations: Subset of queries that is used to change/modify data

## Requirements
* flask
* graphene
* docker
* numpy
* pandas
* tensorflow
* pickle
* gunicorn

## How to run?
First you can train your model. This can be done by running below command in `model` directory:
```
python main.py
```

Then run the flask server by running below command in `api` directory:
```
python server.py
```

Now server is accessible in `0.0.0.0:8080` port.

You can run the apis using postman. Here is an example:
![Untitled](https://user-images.githubusercontent.com/50926437/130287728-50e752c4-85c8-4748-aac4-34645dd2692a.png)



*Amirhossein Abaskohi*
