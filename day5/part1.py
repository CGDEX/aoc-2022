import os 
import sys 
import re 
# I love Windows. 
f = open(os.path.join(sys.path[0],"input2.txt"),"r")
crates, moves = f.read().split("\n\n")
moves = moves.strip().split('\n')
stacks = [] 

for i in range(0,int(re.findall(r'\d+', crates.split('\n')[len(crates.split('\n')) - 1])[-1])):
    stacks.append([])

for i in range(0, len(crates.split('\n')) -1):
    sum = 0
    count = 0
    for j in range(0,len(crates.split('\n')[i])):
        if crates.split('\n')[i][j] == ' ' : 
            count += 1
        if count == 4: 
            count = 0
            sum += 1
        if crates.split('\n')[i][j] == '[' :
            sum += 1
            count = 0   
            stacks[sum - 1].append(crates.split('\n')[i][j + 1]) 

# In the end we will have something like: [['N', 'Z'], ['D', 'C', 'M'], ['P']]
for i in range(0, len(moves)):
    move = re.findall(r'\d+', moves[i]) 
    for j in range(0, int(move[0])):
        value = stacks[int(move[1]) - 1].pop(0)
        stacks[int(move[2]) - 1].insert(0,value)

print("".join(top[0]for top in stacks ))