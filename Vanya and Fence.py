num_friend,len_fence = map(int, input().split()) 
heights_friends = list(map(int, input().split()))  
total = 0
for height in heights_friends:
    if height > len_fence:
        total += 2 
    else:
        total += 1  
print(total)