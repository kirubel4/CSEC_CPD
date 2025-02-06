name = input()
unique = set(name)

if len(unique) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
