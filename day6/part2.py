import os 
import sys 
import re 
# I love Windows. 
f = open(os.path.join(sys.path[0],"input2.txt"),"r")
l = [*f.read()]

count, sum, found = 0, 0, 0
visited = [] 

for i in range(0,len(l)):
    if found == 1:
        break 
    visited = [] 
    count = 0
    visited.append(l[i])
    sum = i + 1
    count += 1
    for j in range(i + 1, len(l)):
        if l[j] not in visited:
            count += 1
            visited.append(l[j])
            sum += 1
        else: 
            break
        if count == 14:
            found = 1
            break

print(sum )