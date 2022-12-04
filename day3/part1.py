import os 
import sys 

# I love Windows. 
f = open(os.path.join(sys.path[0],"input.txt"),"r")
sum = 0 
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for rucksack in f:
    # Example: "vJrwpWtwJgWrhcsFMMfFFhFp" 
    # fist = 'vJrwpWtwJgWr', second = hcsFMMfFFhFp
    first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    sum += letters.index(list(set(first).intersection(second))[0]) + 1  
print(sum)