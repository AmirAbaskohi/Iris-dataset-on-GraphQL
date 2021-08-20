from graphene import ObjectType, Float, Schema, String
from flask import Flask, request
import os
import json
from tensorflow import keras
import pickle
import numpy as np

# Importing our keras classfier for iris dataset
model = keras.models.load_model("../model/iris_classifier.h5")

# Classes to return the result of our neural network
classes = ['Setosa', 'Versicolor', 'Virginica']

# Importing our normalizer to normalize our data
with open('../model/normalizer.pickle', 'rb') as f:
    normalizer = pickle.load(f)

# A graphene query class which is needed for graphql (schema)
class Query(ObjectType):
    # Iris classifier mutation
    iris_class = String(sepal_length=Float(default_value=5.1),
                   sepal_width=Float(default_value=3.5),
                   petal_length=Float(default_value=1.4),
                   petal_width=Float(default_value=0.2))

    # Iris classifier resolver
    def resolve_iris_class(root, info, sepal_length, sepal_width, petal_length, petal_width):
        # Making a list of parameters in a form which is acceptable by normalizer
        values = [[sepal_length, sepal_width, petal_length, petal_width]]
        # Normalizing the data
        values = normalizer.transform(values)
        # Classfing and returning the result
        return classes[np.argmax(model.predict(np.array(values)), axis=1)[0]]

# Creating flas application and making an instance of our Query schema
app = Flask(__name__)
schema = Schema(query=Query)

# Making an route api which uses our schema to return the calue
@app.route("/", methods=["POST"])
def classify():
    # Loading the parameters passed in body of the request
    data = json.loads(request.data)
    # Executing the resolver to find out the iris flower class
    result = schema.execute(data['query'])
    # Return the result with code 200
    return json.dumps(result.data), 200


if __name__ == '__main__':
    # Running our server on 0.0.0.0 and port 8080
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
