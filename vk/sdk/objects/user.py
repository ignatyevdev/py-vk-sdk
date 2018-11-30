from typing import List

from vk.sdk.object import VKObject
from vk.sdk.objects.meta.for_user import Career, City


class User(VKObject):

    def __init__(self, user_data):

        self.id = None                      # идентификатор пользователя
        self.first_name = None              # имя пользователя
        self.last_name = None               # фамилия пользователя

        """
        Поле не пустое, если страница пользователя удалена или заблокирована, содержит значение deleted или banned.
        В этом случае опциональные поля равны None.
        """
        self.deactivated = None

        """
        Скрыт ли профиль пользователя настройками приватности.
        """
        self.is_closed = None

        """
        Может ли текущий пользователь видеть профиль при is_closed = 1 (например, если он есть в друзьях).
        """
        self.can_access_closed = None

        self.about = None                   # содержимое поля «О себе» из профиля
        self.activities = None              # содержимое поля «Деятельность» из профиля

        """
        Дата рождения. В формате D.M.YYYY или D.M (если год рождения скрыт).
        Если дата рождения скрыта целиком, поле имеет значение None.
        """
        self.bdate = None

        """
        информация о том, находится ли текущий пользователь в черном списке. Возможные значения:
        1 — находится;
        0 — не находится.
        """
        self.blacklisted = None

        """
        информация о том, находится ли пользователь в черном списке у текущего пользователя. Возможные значения:
        1 — находится;
        0 — не находится.
        """
        self.blacklisted_by_me = None

        self.books = None                   # содержимое поля «Любимые книги» из профиля пользователя

        """
        информация о том, может ли текущий пользователь оставлять записи на стене. Возможные значения:
        1 — может;
        0 — не может.
        """
        self.can_post = None

        """
        информация о том, может ли текущий пользователь видеть чужие записи на стене. Возможные значения:
        1 — может;
        0 — не может.
        """
        self.can_see_all_posts = None
        self.can_see_audio = None
        self.can_send_friend_request = None
        self.can_write_private_message = None
        self.career: List[Career] = None
        self.city: City = None
        self.common_count = None

        super().__init__(user_data)
