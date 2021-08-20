from graphene import ObjectType, String, Schema, Int
from flask import Flask, request
import os
import json

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"),
    age=Int(default_value=0))
    goodbye = String()

    def resolve_hello(root, info, name, age):
        return f'Hello {name} with age {age}!'

app = Flask(__name__)
schema = Schema(query=Query)

@app.route("/", methods=["POST"])
def hello():
    print("**********************")
    print(request.data)
    print("**********************")
    data = json.loads(request.data)
    print("**********************")
    print(data)
    print("**********************")
    result = schema.execute(data['query'])
    return json.dumps(result.data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))