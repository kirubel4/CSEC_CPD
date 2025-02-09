k, r = map(int, input().split())

for n in range(1, 11):  
    total_price = n * k  
    
    if total_price % 10 == 0 or total_price % 10 == r:
        print(n)
        break  
