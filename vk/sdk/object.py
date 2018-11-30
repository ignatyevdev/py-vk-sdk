

class JSONObject(object):

    __RESERVED_WORDS = {'from': '_from'}

    def __init__(self, data):

        self.__data = data

        if not isinstance(data, dict):
            return

        # {'key': 'value'} -> SomeObject.key = value
        for key, value in data.items():
            # {'key': ['object1', ..., 'objectN']}
            if isinstance(value, (list, tuple)):
                setattr(self, key, [MetaObject(item) if isinstance(item, dict) else item for item in value])
            # {'key': <object>}
            else:
                setattr(self,  (self.__RESERVED_WORDS[key] if key in self.__RESERVED_WORDS else key),
                        MetaObject(value) if isinstance(value, dict) else value)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__data)


class VKObject(JSONObject):

    def __init__(self, object_data):
        super().__init__(object_data)


class MetaObject(JSONObject):

    def __init__(self, meta_data):
        super().__init__(meta_data)
