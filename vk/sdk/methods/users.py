from vk.sdk.methods.users_methods import users_get, users_get_followers


def get():
    return users_get.MethodExecutor()


def get_followers():
    return users_get_followers.MethodExecutor()
