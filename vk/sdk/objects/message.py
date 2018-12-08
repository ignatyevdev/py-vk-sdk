"""

API Version: 5.80+

"""
from typing import List

from vk.sdk.object import VKObject
from vk.sdk.objects.meta.general import Geo
from vk.sdk.objects.meta.for_message import Action


class Message(VKObject):

    def __init__(self, message_data):
        self.id = None
        self.date = None
        self.peer_id = None
        self.from_id = None
        self.text = None
        self.random_id = None
        self.ref = None
        self.ref_source = None
        self.attachments = None                 # List[Attachment]
        self.important = None
        self.geo: Geo= None
        self.payload = None
        self.fwd_messages: List[Message] = None
        self.reply_message: Message = None
        self.action: Action = None
        super().__init__(message_data)
