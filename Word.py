s = input()
upper_count = 0
for c in s:
    if c.isupper():
        upper_count += 1
lower_count = len(s) - upper_count
if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())
