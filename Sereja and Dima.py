n = int(input())  
arr = list(map(int, input().split()))  

l, r = 0, n - 1  
s, d = 0, 0  
turn = True  

while l <= r:
    if arr[l] > arr[r]:
        val = arr[l]
        l += 1
    else:
        val = arr[r]
        r -= 1

    if turn:
        s += val
    else:
        d += val

    turn = not turn  

print(s, d)
