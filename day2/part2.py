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
# X - Lose
# Y - Draw
# Z - Win
beats = ['X','Y','Z']
# A -> Z
# B -> X
# C -> Y
scores = {
    'Z' : 3,
    'Y' : 2,
    'X' : 1
}
weakness = [{'A' : 'Z', 'B' : 'X', 'C' : 'Y'}, {'A' : 'X', 'B' : 'Y', 'C' : 'Z'}, {'A' : 'Y', 'B' : 'Z', 'C' : 'X'}]
score = 0 

for l in f: 
    left, right = l.split()
    score += 3 * beats.index(right) + scores[weakness[beats.index(right)][left]]
print(score)