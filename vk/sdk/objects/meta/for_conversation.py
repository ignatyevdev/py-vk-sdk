from typing import List

from vk.sdk.object import MetaObject


class Peer(MetaObject):

    def __init__(self, peer_data):
        self.id = None
        self.type = None
        self.local_id = None
        super().__init__(peer_data)


class PushSettings(MetaObject):

    def __init__(self, push_settings_data):
        self.disabled_until = None
        self.disabled_forever = None
        self.no_sound = None
        super().__init__(push_settings_data)


class CanWrite(MetaObject):

    def __init__(self, can_write_data):
        self.allowed = None
        self.reason = None
        self.local_id = None
        super().__init__(can_write_data)


class ChatSettings(MetaObject):

    def __init__(self, chat_settings_data):
        self.members_count = None
        self.title = None
        self.pinned_message = None              # objects.Message
        self.state = None
        self.photo = None                       # objects.Photo
        self.active_ids: List[int] = None
        self.is_group_channel = None
        super().__init__(chat_settings_data)
