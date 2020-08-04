from api import get_resource_with_id, get_all_resources
from load_open311_resources import load_resources
from pprint import pprint
import logging

# load open311 schema and urls of cities that implemented open311 spec
schema, cities = load_resources()
vanilla_schema = {field_name: {"type": "string"} for field_name in schema["properties"]}


def validate_cities_with_schema(city, url, resource):
    validate_schema = []
    city_impl = get_resource_with_id(url["url"], "requests")
    for attr in city_impl:
        if attr not in vanilla_schema:
            validate_schema.append(False)
        validate_schema.append(True)
    assert (any(validate_schema))
    print(f"city: {city} schema valid for requests")


for city_name, city_url in cities.items():
    validate_cities_with_schema(city_name, city_url)

# Create dictionary with location and url params
# Run asserts on schema v. location response
# Keep some running total of location: resource: bool indication if resource difference (data frame?)
# location | resource name | difference |
# --------------------------------------
# some sort of aggregation?
