import requests

# https://[API endpoint]/services.[format]
# https://[API endpoint]/services/id.[format]


def build_open311_resources_url(api_endpoint, resource):
    return f'{api_endpoint}{resource}.json'


def get_all_resources(api_endpoint, resource):
    return requests.get(build_open311_resources_url(api_endpoint, resource)).json()


def get_resource_with_id(api_endpoint, resource):
    return get_all_resources(api_endpoint, resource)[0]