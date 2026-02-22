arr = [1,2,3]

arr.append(4)
arr.pop()
arr.reverse() 

arr[1:3]


freq = {}
freq['a'] = freq.get('a', 0) + 1


s = set()
s.add(5)

stack = []
stack.append(10)
stack.pop()

from collections import deque
q = deque()
q.append(10)
q.popleft()




print(arr)
print(freq)
print(s)
print(stack)
print(q)