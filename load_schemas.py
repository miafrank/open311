import json


def load_resources():
    with open('schemas/request_schema.json') as request_schema:
        request_schema = json.load(request_schema)

    with open('schemas/service_schema.json') as service_schema:
        service_schema = json.load(service_schema)

    with open('schemas/service_definition_schema') as service_definition_schema:
        service_definition_schema = json.load(service_definition_schema)

    with open('open311_cities') as open311_cities:
        cities = json.load(open311_cities)

    return request_schema, service_schema, service_definition_schema, cities

