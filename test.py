users = [
    {'id': 1,
    'name': 'Tunga',
    'surname': 'Chan',
    'age': '24'}
]

def us(user_id: int):
    cur_user = list(filter(lambda user: user.get('id') == user_id, users))[0]
    print(cur_user['name'])

us(1)