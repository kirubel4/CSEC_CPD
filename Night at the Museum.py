s = input()
pos = 'a'
rotations = 0
for c in s:
    cw = abs(ord(c) - ord(pos))
    ccw = 26 - cw
    rotations += min(cw, ccw)
    pos = c  
print(rotations)
