exhibit_name = input()

current_position = 'a'
total_rotations = 0

for letter in exhibit_name:
    clockwise_distance = abs(ord(letter) - ord(current_position))
    counterclockwise_distance = 26 - clockwise_distance
    total_rotations += min(clockwise_distance, counterclockwise_distance)
    current_position = letter  # Move the pointer to the new letter

print(total_rotations)
