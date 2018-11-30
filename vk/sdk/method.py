from vk.sdk import api
from vk.sdk.object import VKObject
from vk.sdk.error import ApiError, RequestError

from typing import List


class Method:

    def __init__(self, name, required_params=None):
        self.__name = name
        self.__required_params = ['v', 'access_token'] + (required_params if required_params is not None else list())
        self.__params = dict()

    def get_name(self):
        return self.__name

    def get_required_params(self):
        return self.__required_params

    def get_params(self):
        return self.__params

    def add_param(self, name: str, value: str):
        self.__params[name] = value
        return self

    def execute(self) -> VKObject or List[VKObject]:

        for required_param in self.get_required_params():
            if required_param not in self.get_params():
                raise RequestError('\nНе все требуемые параметры были указаны.\nТребуемые параметры: {}\nВы указали: {}'
                                   .format(self.get_required_params(), self.get_params()))

        result = api.call_method(self.get_name(), **self.get_params())

        # {response: {count: <int>, items: [...]}}
        if 'items' in result:
            # {response: {count: <int>, items: [<object1>, <object2>, ..., <objectN>]}}
            if isinstance(result['items'], (list, tuple)):
                objects = [(VKObject(item) if isinstance(item, dict) else item) for item in result['items']]
                return objects
        else:
            # {response: <object>}
            # {response: {key1: <value1>, ..., keyN: <valueN>}}
            if isinstance(result, dict):
                obj = VKObject(result)
                return obj
            # {response: [<object1>, <object2>, ..., <objectN>]}
            elif isinstance(result, (list, tuple)):
                objects = [(VKObject(item) if isinstance(item, dict) else item) for item in result]
                return objects

        # {response: <str:int>}
        return result

    def access_token(self, access_token):
        return self.add_param('access_token', access_token)

    def version(self, version):
        return self.add_param('v', version)

    def lang(self, lang):
        return self.add_param('lang', lang)

    def test_mode(self, test_mode):
        return self.add_param('test_mode', test_mode)


class CountAndOffsetSupportMethod(Method):

    def __init__(self, name, required_params=None):
            super().__init__(name, required_params)

    def count(self, count):
        return self.add_param('count', count)

    def offset(self, offset):
        return self.add_param('offset', offset)
