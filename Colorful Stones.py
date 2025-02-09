stones = input().strip()
commands = input().strip()

current_position = 1  

for command in commands:
    if stones[current_position - 1] == command:
        current_position += 1  

print(current_position)
