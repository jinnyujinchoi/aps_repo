from collections import deque

q = deque()
q.append(1)     # enqueue()
t = q.popleft() # dequeue()

# list_q = []
# for i in range(1000000):
#     list_q.append(i)
# for _ in range(10000):
#     list_q.pop(0)
# print('end')
deque_q = deque()               # 이 방법이 짱 빠름!
for i in range(1000000):
    deque_q.append(i)
for _ in range(1000000):
    deque_q.popleft()
print('end')