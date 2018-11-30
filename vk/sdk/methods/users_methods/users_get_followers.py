from vk.sdk.method import CountAndOffsetSupportMethod
from vk.sdk.objects.user import User

from typing import List


class MethodExecutor(CountAndOffsetSupportMethod):

    __MY_NAME = 'users.getFollowers'

    def __init__(self):
        super().__init__(self.__MY_NAME)

    def user_id(self, user_id):
        return self.add_param('user_id', user_id)

    def fields(self, fields):
        return self.add_param('fields', fields)

    def num_case(self, num_case):
        return self.add_param('num_case', num_case)

    def execute(self) -> List[User]:
        object_list = super().execute()
        return [User(obj.__dict__) for obj in object_list]
