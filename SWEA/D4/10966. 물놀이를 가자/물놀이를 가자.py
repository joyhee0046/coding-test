## 한상오빠 코드
# import sys
# sys.stdin = open('sample_input.txt', 'r')

from collections import deque
 
def bfs():
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1:
                distance[nx][ny] = distance[cx][cy] + 1
                queue.append((nx, ny))

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    maps = [list(input()) for _ in range(N)]
    # 거리를 계산할 distance 테이블
    distance = [[-1] * M for _ in range(N)]
    queue = deque()
    # 최종 거리
    answer = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'W':
                distance[i][j] = 0
                queue.append((i, j))
 
    bfs()
 
    for i in range(N):
        for j in range(M):
            answer += distance[i][j]
 
    print(f'#{test_case} {answer}')