from graphene import ObjectType, String, Schema, Int

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"),
    age=Int(default_value=0))
    goodbye = String()

    def resolve_hello(root, info, name, age):
        return f'Hello {name} with age {age}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

def main():
    schema = Schema(query=Query)
    result = schema.execute('{ hello }')
    print(result.data['hello'])


if __name__ == '__main__':
    main()