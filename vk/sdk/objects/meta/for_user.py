from vk.sdk.object import MetaObject


class Career(MetaObject):

    def __init__(self, meta_data):
        self.group_id = None
        self.company = None
        self.country_id = None
        self.city_id = None
        self.city_name = None
        self._from = None
        self.until = None
        self.position = None
        super().__init__(meta_data)


class City(MetaObject):

    def __init__(self, meta_data):
        self.id = None
        self.title = None
        super().__init__(meta_data)
