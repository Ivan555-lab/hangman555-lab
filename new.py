users = {
    'a': {
        'f':'a',
        'l':'e',
        'loc':'l',
    },
    'm': {
        'f':'m',
        'l':'c',
        'loc': 'p'
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['f'] + " " + user_info['l']
    location = user_info['loc']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())










