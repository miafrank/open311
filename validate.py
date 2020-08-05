from api import get_resource_response, get_resource_response_with_id
from load_schemas import load_resources
import logging

logging.basicConfig(level=logging.INFO)

# load open311 schema and urls of cities that implemented open311 spec
request_schema, service_schema, service_definition_schema, cities = load_resources()
og_request_schema = {field_name: {"type": "string"} for field_name in request_schema["properties"]}
og_service_schema = {field_name: {"type": "string"} for field_name in service_schema["properties"]}
og_service_definition_schema = {field_name: {"type": "string"}
                                for field_name in service_definition_schema["properties"]["attributes"]["items"]["properties"]}


def validate_cities_with_schema(city, resource, api_response, schema):
    validate_schema = []
    for attr in api_response:
        if attr not in schema:
            validate_schema.append(False)
        validate_schema.append(True)

    assert all(validate_schema)
    logging.info(f" city: {city} schema valid for resource: /{resource}")


for city_name, city_url in cities.items():
    validate_cities_with_schema(city=city_name,
                                resource="requests",
                                schema=og_request_schema,
                                api_response=get_resource_response(city_url.get("url"), "requests"))
    validate_cities_with_schema(city=city_name,
                                resource="services",
                                schema=og_service_schema,
                                api_response=get_resource_response(city_url.get("url"), "services"))
    validate_cities_with_schema(city=city_name,
                                resource="service definition",
                                schema=og_service_definition_schema,
                                api_response=get_resource_response_with_id(city_url.get("url"), "services", city_name))
