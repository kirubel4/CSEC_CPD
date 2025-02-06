nums = int(input())  
cubes = list(map(int, input().split()))  
cubes.sort()  

for num in cubes:
    print(num, end=" ")
