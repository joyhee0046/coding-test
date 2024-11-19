from itertools import combinations
from collections import deque

# 입력 받기
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 바이러스를 놓을 수 있는 위치와 빈 칸의 개수 계산
virus_positions = []
empty_count = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_positions.append((i, j))
            lab[i][j] = 0
            empty_count += 1
        elif lab[i][j] == 0:
            empty_count += 1

# 이동 방향 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# BFS 함수
def bfs(selected_viruses):
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    # 초기 바이러스 위치
    for x, y in selected_viruses:
        queue.append((x, y, 0))
        visited[x][y] = 0

    time = 0
    spread_count = 0

    while queue:
        x, y, t = queue.popleft()
        # 현재까지의 최대 시간 기록
        time = max(time, t)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if lab[nx][ny] == 0 or lab[nx][ny] == 2:
                    visited[nx][ny] = t + 1
                    queue.append((nx, ny, t + 1))
                    # if lab[nx][ny] == 0:  # 빈 칸을 채운 경우만 증가
                    spread_count += 1

    # 모든 빈 칸이 채워졌는지 확인
    return time if spread_count == empty_count-M else float('inf')


# 최소 시간 계산
min_time = float('inf')
for viruses in combinations(virus_positions, M):
    min_time = min(min_time, bfs(viruses))

# 결과 출력
print(min_time if min_time != float('inf') else -1)

