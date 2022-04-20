responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("which?")

    responses[name] = response
    repeat = input("Would? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

    print("\n---Poll Results---")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")










