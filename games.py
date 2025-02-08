n = int(input())
uniforms = []

for _ in range(n):
    home, guest = map(int, input().split())
    uniforms.append((home, guest))

switch_count = 0

for host in uniforms:
    for visitor in uniforms:
        if host != visitor and host[0] == visitor[1]:
            switch_count += 1

print(switch_count)
