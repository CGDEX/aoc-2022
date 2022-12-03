import os 
import sys 

# I love Windows. 
f = open(os.path.join(sys.path[0],"input.txt"),"r")
sum = 0 
top = 0 

# 1 - rock (A - npc, X - player)
# 2 - paper (B - npc, Y - player)
# 3 - scissors (C - npc, Z - player) 
# 0 - lost 
# 3 - draw
# 6 - win 
# Rock defeats scissors, scissors defeats paper and paper defeats rock
beats = [[('Z','A'), ('Y','C'), ('X','B')], [('X', 'A'), ('Y', 'B'), ('Z','C')], [('X','C'), ('Z','B'), ('Y','A')]]
scores = {
    'Z' : 3,
    'Y' : 2,
    'X' : 1
}
score = 0 

for l in f: 
    left, right = l.split()
    score += 3*(next(i for i,v in enumerate(beats) if (right,left) in v)) + scores[right]

print(score)