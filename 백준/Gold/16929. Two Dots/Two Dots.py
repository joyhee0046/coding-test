import sys
# 파이썬의 기본 재귀 깊이 제한을 높여서 큰 입력에도 대비
sys.setrecursionlimit(10000)

# 깊이 우선 탐색(DFS) 함수 정의
def dfs(x, y, px, py, color):
    """
    현재 위치 (x, y)에서 DFS 탐색을 진행하여 사이클을 찾는 함수

    x, y: 현재 위치
    px, py: 이전 위치 (바로 전에 방문한 위치)
    color: 현재 탐색 중인 색상
    """
    # 이미 방문한 노드라면 사이클이 있다는 의미이므로 True 반환
    if visited[x][y]:
        return True

    # 현재 노드를 방문 처리
    visited[x][y] = True

    # 상하좌우 네 방향으로 이동하며 DFS 탐색 진행
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # 새로운 좌표 nx, ny로 이동
        nx, ny = x + dx, y + dy

        # 새로운 좌표가 게임판 내부에 있어야 하고
        # 이전 방문 위치가 아니어야 하며
        # 색상이 동일한 경우에만 탐색을 이어감
        if 0 <= nx < N and 0 <= ny < M and (nx, ny) != (px, py) and board[nx][ny] == color:
            # 만약 새로운 좌표가 이미 방문한 곳이거나 DFS 탐색을 통해 사이클이 발견되면 True 반환
            if visited[nx][ny] or dfs(nx, ny, x, y, color):
                return True

    # 네 방향을 모두 탐색했으나 사이클이 없다면 False 반환
    return False

# 입력 처리
N, M = map(int, input().split())  # N은 게임판의 행 수, M은 열 수
board = [list(input().strip()) for _ in range(N)]  # 게임판 상태를 입력 받음
visited = [[False] * M for _ in range(N)]  # 방문 여부를 체크하는 2차원 배열, 초기에는 모두 False

# 모든 좌표에 대해 DFS 탐색을 진행
for i in range(N):
    for j in range(M):
        # 만약 현재 위치를 방문하지 않았다면 DFS 탐색 시작
        if not visited[i][j]:
            # DFS 탐색 중 사이클이 발견되면 즉시 "Yes"를 출력하고 프로그램 종료
            if dfs(i, j, -1, -1, board[i][j]):  # 시작할 때는 이전 위치가 없으므로 (-1, -1)을 전달
                print("Yes")
                sys.exit()  # 사이클이 존재하면 더 이상 탐색할 필요가 없으므로 프로그램을 종료

# 모든 좌표를 탐색했으나 사이클이 없다면 "No" 출력
print("No")
