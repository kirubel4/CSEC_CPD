a, b, c, d = map(int, input().split())
unique_horseshoes = {a, b, c, d}
needed_horseshoes = 4 - len(unique_horseshoes)
print(needed_horseshoes)
