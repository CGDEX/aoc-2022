import os 
import sys 
import time

# I love Windows. 
f = open(os.path.join(sys.path[0],"input.txt"),"r")
total = 0 

for l in f:
    first, second = l.split(',')
    (begin1, end1), (begin2, end2) = [int(i) for i in first.split('-')], [int(i) for i in second.split('-')]
    if (begin2 >= begin1 and begin2 <= end1) or (end2 >= begin1 and end2 <= end1) or (begin1 >= begin2 and begin1 <= end2):
        total += 1

print(total)


# Examples
# 5-7, 7-9  begin2 >= begin1 and begin2 <= end1  
# 2-8, 3-7  begin2 >= begin1 and begin2 <= end1
# 6-6, 4-6  end2 >= begin1 and end2 <= end1 
# 2-6, 4-8  begin2 >= begin1 and begin2 <= end1
# 6-6, 6-7  begin2 >= begin1 and begin2 <= end1
# 4-8, 2-9  begin1 >= begin2 and begin1 <= end2
