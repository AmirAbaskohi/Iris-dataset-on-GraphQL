from graphene import ObjectType, String, Schema, Int
from flask import Flask
import os

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"),
    age=Int(default_value=0))
    goodbye = String()

    def resolve_hello(root, info, name, age):
        return f'Hello {name} with age {age}!'

app = Flask(__name__)
schema = Schema(query=Query)

@app.route("/", methods=["GET"])
def hello():
    result = schema.execute('{ hello(name: "amirhossein", age: 21) }')
    return '{"result": "' + result.data['hello'] + '"}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))