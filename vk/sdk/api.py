import json
import urllib.parse
import urllib.request

from vk.sdk.error import ApiError


def call_method(method_name, **params):
    endpoint = "https://api.vk.com/method/"
    query = urllib.parse.urlencode(params)
    url = endpoint + method_name + "?" + query

    result = json.loads(urllib.request.urlopen(url).read())

    if 'error' in result:
        error = result['error']
        raise ApiError(error['error_code'], error['error_msg'], error['request_params'])

    return result['response']
