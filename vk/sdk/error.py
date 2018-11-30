

class VKError(Exception):

    def __init__(self, error_message):
        super().__init__(error_message)
        self.__error_message = error_message

    def get_message(self):
        return self.__error_message


class RequestError(VKError):

    def __init__(self, error_message):
        super().__init__(error_message)


class ApiError(VKError):

    def __init__(self, error_code, error_message, request_params):
        super().__init__(error_message)
        self.__error_code = error_code
        self.__request_params = request_params

    def get_code(self):
        return self.__error_code

    def get_request_params(self):
        return self.__request_params

    def __str__(self):
        return "\nКод ошибки = {}\nСообщение ошибки = {}\nПараметры запроса = {}"\
            .format(self.get_code(), self.get_message(), self.get_request_params())
