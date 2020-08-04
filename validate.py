from api import get_resource_response
from load_schemas import load_resources
import logging

logging.basicConfig(level=logging.INFO)

# load open311 schema and urls of cities that implemented open311 spec
request_schema, service_schema, cities = load_resources()
og_request_schema = {field_name: {"type": "string"} for field_name in request_schema["properties"]}
og_service_schema = {field_name: {"type": "string"} for field_name in service_schema["properties"]}


def validate_cities_with_schema(city, url, resource, schema):
    validate_schema = []
    city_impl = get_resource_response(url.get("url"), resource)
    for attr in city_impl:
        if attr not in schema:
            validate_schema.append(False)
        validate_schema.append(True)
    assert any(validate_schema)
    logging.info(f" city: {city} schema valid for {resource}")


for city_name, city_url in cities.items():
    # validate_cities_with_schema(city_name, city_url, "requests", og_request_schema)
    validate_cities_with_schema(city_name, city_url, "services", og_service_schema)