a, b = map(int, input().split())

max_roll = max(a, b)

favorable_outcomes = 6 - max_roll + 1  
total_possibilities = 6  

gcd = __import__('math').gcd(favorable_outcomes, total_possibilities)

print(f"{favorable_outcomes // gcd}/{total_possibilities // gcd}")
