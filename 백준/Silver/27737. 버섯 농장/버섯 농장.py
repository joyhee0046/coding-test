'''
나머지를 더하면 안됨.
나머지가 0이 아니면 그냥 1을 더해야함.
'''



from collections import deque

def bfs(x, y, board, visited, n):
    # BFS로 연결된 칸을 모두 탐색하여 구역의 크기를 반환
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1  # 현재 구역의 크기
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    return size

# 입력 처리
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 방문 배열과 구역 크기 저장 리스트 초기화
visited = [[False] * n for _ in range(n)]
regions = []

# 모든 버섯이 자랄 수 있는 구역의 크기를 구하여 regions에 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 0 and not visited[i][j]:
            region_size = bfs(i, j, board, visited, n)
            regions.append(region_size)

# 각 구역을 덮기 위해 필요한 최소 포자 수 계산
needed_spores = 0
for size in regions:
    if size % k == 0:
        needed_spores += (size // k)
    else :
        needed_spores += (size // k)+1

# 결과 출력
if (needed_spores > m) | (needed_spores == 0):
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(m - needed_spores)  # 남은 포자의 개수