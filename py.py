n = int(input())
mi = 0
ch = 0
for _ in range(n):
    m,c = map(int, input().split())
    if m > c:
        mi += 1
    elif c > m:
        ch += 1
    else:
        continue
if mi > ch:
    print("Mishka")
elif ch > mi:
    print("Chris")
else:
    print("Friendship is magic!^^")