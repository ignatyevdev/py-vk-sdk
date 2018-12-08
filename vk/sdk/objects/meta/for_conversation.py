from typing import List

from vk.sdk.object import MetaObject
from vk.sdk.objects.message import Message
from vk.sdk.objects.meta.general import Photo


class Peer(MetaObject):

    def __init__(self, meta_data):
        self.id = None
        self.type = None
        self.local_id = None
        super().__init__(meta_data)


class PushSettings(MetaObject):

    def __init__(self, meta_data):
        self.disabled_until = None
        self.disabled_forever = None
        self.no_sound = None
        super().__init__(meta_data)


class CanWrite(MetaObject):

    def __init__(self, meta_data):
        self.allowed = None
        self.reason = None
        self.local_id = None
        super().__init__(meta_data)


class ChatSettings(MetaObject):

    def __init__(self, data):
        self.members_count = None
        self.title = None
        self.pinned_message: Message = None
        self.state = None
        self.photo: Photo = None
        self.active_ids: List[int] = None
        self.is_group_channel = None
        super().__init__(data)
