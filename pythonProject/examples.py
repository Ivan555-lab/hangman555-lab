jack = {
    'name': 'jack',
    'car': 'bmw'
}

john = {
    'name': 'john',

}

users = ['jack', 'oun']



# j_n = [u for u in users if u.startswith('o')]
# print(j_n)

new_names = []
for u in users:
    if u.startswith('o'):
        new_names.append(u)

print(new_names)

