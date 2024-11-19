from collections import deque

# 입력 받기
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# 동전 위치 찾기
coins = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

# 이동 방향 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 탐색
def bfs():
    queue = deque([(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)])  # 동전1 x,y / 동전2 x,y / 버튼 횟수
    visited = set([(coins[0][0], coins[0][1], coins[1][0], coins[1][1])])    # 방문 상태

    while queue:
        x1, y1, x2, y2, count = queue.popleft()
        
        # 버튼을 10번 초과하면 실패
        if count >= 10:
            return -1
        
        for dx, dy in directions:
            # 새 위치 계산
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy

            # 경계 체크
            out1 = not (0 <= nx1 < N and 0 <= ny1 < M)  # 동전1이 보드 밖으로 나갔는가
            out2 = not (0 <= nx2 < N and 0 <= ny2 < M)  # 동전2가 보드 밖으로 나갔는가
            
            if out1 and out2:  # 두 동전 모두 떨어지면 무시
                continue
            if out1 or out2:  # 한 동전만 떨어지면 성공
                return count + 1
            
            # 벽 체크
            if not out1 and board[nx1][ny1] == '#':  # 동전1이 벽에 부딪히면 제자리
                nx1, ny1 = x1, y1
            if not out2 and board[nx2][ny2] == '#':  # 동전2가 벽에 부딪히면 제자리
                nx2, ny2 = x2, y2

            # 새로운 상태를 큐에 추가
            if (nx1, ny1, nx2, ny2) not in visited:
                visited.add((nx1, ny1, nx2, ny2))
                queue.append((nx1, ny1, nx2, ny2, count + 1))
    
    return -1  # 탐색 종료 후에도 성공하지 못한 경우

# 결과 출력
print(bfs())
