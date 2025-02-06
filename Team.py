num_problem = int(input())  
count = 0  

for _ in range(num_problem):  
    num_1, num_2, num_3 = map(int, input().split())  
    if num_1+ num_2+ num_3 >= 2:  
        count += 1  

print(count)  
