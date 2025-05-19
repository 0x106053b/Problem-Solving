# (1) 

N, K = map(int, input().split())
people = list(range(1, N+1))
answer = []
while len(people) > 0:
    index = (K-1) % len(people)
    answer.append(str(people[index]))
    del people[index]
    people = people[index:] + people[:index]

print("<" + ", ".join(answer) + ">")

# (2)

from collections import deque

N, K = map(int, input().split())
people = deque(range(1, N+1))
answer = []
while len(people) > 0:
    for _ in range(K-1): people.append(people.popleft())
    answer.append(people.popleft())

print('<'+', '.join(map(str, answer))+'>')