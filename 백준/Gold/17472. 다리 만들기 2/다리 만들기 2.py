import sys
from collections import deque

def check(li):
    start, cnt = 0, 0
    for idx in range(len(li)):
        if li[idx] > 0:  # 섬을 만난 경우
            if start > 0 and start != li[idx] and cnt >= 2:  # 다리 조건
                edge.append((start, li[idx], cnt))
            start, cnt = li[idx], 0
        elif start > 0:  # 바다를 만나면 다리 길이 증가
            cnt += 1

def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]

def union(v1, v2, w):
    global answer
    root1, root2 = find(v1), find(v2)
    if root1 != root2:
        answer += w
        if rank[root1] < rank[root2]:
            parents[root1] = root2
            rank[root2] += rank[root1]
        else:
            parents[root2] = root1
            rank[root1] += rank[root2]

N, M = map(int, input().split())
country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 1
queue = deque()
edge = []

# 섬 고유번호 설정
visited = [[False] * M for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(M):
        if country[i][j] == 1 and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = True
            while queue:
                r, c = queue.popleft()
                country[r][c] = cnt
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and country[nr][nc] == 1 and not visited[nr][nc]:
                        queue.append((nr, nc))
                        visited[nr][nc] = True
            cnt += 1

# 행과 열에서 다리 탐색
for row in country:
    check(row)
for col in zip(*country):
    check(col)

# 크루스칼 알고리즘
edge = sorted(edge, key=lambda x: x[2])
parents = [i for i in range(cnt)]
rank = [1] * cnt
answer = 0

for e in edge:
    union(e[0], e[1], e[2])

# 모든 섬이 연결되었는지 확인
roots = set(find(i) for i in range(1, cnt))
if len(roots) > 1:
    print(-1)
else:
    print(answer)
