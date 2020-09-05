from collections import deque

q = deque(maxlen=5) #고정크기의 큐
q.append(1)
q.append(2)
for i in range(3, 10):
    q.append(i)
print(q)

#appendleft(), append(), popleft(), pop()
#시간복잡도 O(1), 리스트의 경우 O(N)

d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())

print(d)