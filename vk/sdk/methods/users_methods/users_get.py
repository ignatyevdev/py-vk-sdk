from vk.sdk.method import Method
from vk.sdk.objects.user import User
from typing import List


class MethodExecutor(Method):

    __MY_NAME = 'users.get'

    def __init__(self):
        super().__init__(self.__MY_NAME)

    def user_ids(self, user_ids):
        return self.add_param('user_ids', user_ids)

    def fields(self, fields):
        return self.add_param('fields', fields)

    def name_case(self, name_case):
        return self.add_param('name_case', name_case)

    def execute(self) -> List[User]:
        object_list = super().execute()
        return [User(obj.__dict__) for obj in object_list]
