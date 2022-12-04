import os 
import sys 

# I love Windows. 
f = open(os.path.join(sys.path[0],"input.txt"),"r")
total = 0 
for l in f:
    first, second = l.split(',')
    (begin1, end1), (begin2, end2) = [int(i) for i in first.split('-')], [int(i) for i in second.split('-')]
    if (begin2 >= begin1 and begin2 <= end1 and end2 >= begin1 and end2 <= end1) or (begin1 >= begin2 and begin1 <= end2 and end1 >= begin2 and end1 <= end2):
        total += 1
print(total)


# Examples
# 2-8 , 3-7 => [2,3,4,5,6,7,8] and [3,4,5,6,7,8]
# 6-6 , 4-6 => [6] and [4,5,6]
