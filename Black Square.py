calories = list(map(int, input().split()))  
game_sequence = input()  
total_calories = 0  
for c in game_sequence:  
    index = int(c) - 1  
    total_calories += calories[index]  
print(total_calories)
