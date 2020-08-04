import json


def load_resources():
    with open('request_schema.json') as request_schema:
        schema = json.load(request_schema)

    with open('open311_cities') as open311_cities:
        cities = json.load(open311_cities)

    return schema, cities

