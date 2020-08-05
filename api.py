import requests
from pprint import pprint
# https://[API endpoint]/services.[format]
# https://[API endpoint]/services/id.[format]


def build_open311_resources_url(api_endpoint, resource):
    return f'{api_endpoint}{resource}.json'


def build_open311_resources_url_with_id(api_endpoint, resource, service_id):
    return f'{api_endpoint}{resource}/' \
           f'{service_id}.json'


def get_resource_response(api_endpoint, resource):
    return requests.get(build_open311_resources_url(api_endpoint, resource)).json()[0]


def get_resource_response_with_id(api_endpoint, resource, city):
    service_id = get_resource_response(api_endpoint, resource)["service_code"]
    if city == 'bloomington':
        service_id = '37'
    if city == 'peoria':
        service_id = '51'
    return requests.get(build_open311_resources_url_with_id(api_endpoint, resource, service_id)).json()["attributes"][0]
