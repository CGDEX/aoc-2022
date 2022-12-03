import os 
import sys 

# I love Windows. 
f = open(os.path.join(sys.path[0],"input.txt"),"r")
sum = 0 
top = 0 

for l in f: 
    if l in ['\n','\r', '\r\n']:
        if sum > top:
            top = sum
        sum = 0 
    else : 
        sum += int(l)

print(top)