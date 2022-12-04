import os 
import sys 
import time

# I love Windows. 
f = open(os.path.join(sys.path[0],"input.txt"),"r")
sum = 0 
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lines = f.readlines()

for i in range(0, len(lines), 3):
    sum += letters.index(list(set(lines[i].strip()).intersection(lines[i+1].strip()).intersection(lines[i+2]))[0])+1

print(sum)