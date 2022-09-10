from collections import deque

def solution(priorities, location):
    answer = 0
    
    arr = [[i, v] for v, i in enumerate(priorities)]
    q = deque(arr)
    max_val = max(q)[0]
    while q:
        max_val = max(q)[0]
        val, idx = q.popleft()
        if val != max_val:
            q.append([val, idx])
        else:
            if idx == location:
                return answer + 1
            else:
                answer += 1