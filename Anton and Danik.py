num_game = int(input())
result = input().strip() 
anton_wins = result.count('A')
danik_wins = result.count('D')
if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
