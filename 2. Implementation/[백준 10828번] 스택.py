import sys
from collections import deque

stack = deque([])

for _ in range(int(input())):
    command = sys.stdin.readline().split()
    try:
        if command[0] == "push": stack.append(command[1])
        elif command[0] == "top": print(stack[-1])
        elif command[0] == "size": print(len(stack))
        elif command[0] == "empty": print(0 if len(stack) else 1)
        elif command[0] == "pop": print(stack.pop())
    except:
        print(-1)