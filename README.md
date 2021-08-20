# GraphQL
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
