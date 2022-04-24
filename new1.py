from new import get_formatted_name

print("Ent q")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("giv a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
