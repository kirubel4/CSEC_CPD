n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    left = y
    right = a[x] - y - 1

    if x > 0:
        a[x - 1] += left
    if x < n - 1:
        a[x + 1] += right

    a[x] = 0

for count in a:
    print(count)
