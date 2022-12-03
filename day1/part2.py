import os 
import sys
import heapq 

# I love Windows. 
f = open(os.path.join(sys.path[0],"input.txt"),"r")
count = 0 
top3 = [0,1,2]

# Heapq documentation: https://docs.python.org/3/library/heapq.html
heapq.heapify(top3)

for l in f: 
    if l in ['\n','\r', '\r\n']:
        smallest_element = heapq.heappop(top3)
        heapq.heappush(top3,max(smallest_element, count))
        count = 0 
    else : 
        count += int(l)

print(sum(top3))