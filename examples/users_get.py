import vk.sdk.methods.users as users

access_token = 'ACCESS_TOKEN'

user = users.get().user_ids(1).fields('career, city').access_token(access_token).version('5.92').execute()[0]

print(user)
print('{} {}'.format(user.first_name, user.last_name))
