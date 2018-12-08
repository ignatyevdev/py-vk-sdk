from typing import List

from vk.sdk.object import VKObject
from vk.sdk.objects.meta.for_conversation import Peer, PushSettings, CanWrite, ChatSettings


class Conversation(VKObject):

    def __init__(self, conversation_data):
        self.peer: Peer = None
        self.in_read = None
        self.out_read = None
        self.unread_count = None
        self.important = None
        self.unanswered = None
        self.push_settings: PushSettings = None
        self.can_write: CanWrite = None
        self.chat_settings: ChatSettings = None
        super().__init__(conversation_data)
