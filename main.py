from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

def main():
    schema = Schema(query=Query)
    result = schema.execute('{ hello }')
    print(result.data['hello'])


if __name__ == '__main__':
    main()