from vk.sdk.object import MetaObject

from vk.sdk.objects.meta.general import Photo


class Action(MetaObject):

    def __init__(self, meta_data):
        self.type = None
        self.member_id = None
        self.text = None
        self.email = None
        self.photo = None
        super().__init__(meta_data)
