from vk.sdk.object import MetaObject


class Photo(MetaObject):

    def __init__(self, data):
        self.photo_50 = None
        self.photo_100 = None
        self.photo_200 = None
        super().__init__(data)


class Place(MetaObject):
    def __init__(self, meta_data):
        self.id = None
        self.title = None
        self.latitude = None
        self.longitude = None
        self.created = None
        self.icon = None
        self.country = None
        self.city = None
        # Если место добавлено как чекин в сообщество, объект place имеет дополнительные поля:
        self.type = None
        self.group_id = None
        self.group_photo = None
        self.checkins = None
        self.updated = None
        self.address = None
        super().__init__(meta_data)


class Geo(MetaObject):

    def __init__(self, meta_data):

        self.type = None
        self.coordinates = None
        self.place: Place = None
        super().__init__(meta_data)
