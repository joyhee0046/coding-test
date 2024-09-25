from collections import deque

# 나이트가 이동할 수 있는 8가지 방향 (x축, y축)
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def bfs(l, start, end):
    # 출발지와 목적지가 같으면 이동할 필요가 없으므로 바로 0 반환
    if start == end:
        return 0

    # 방문 여부를 기록하기 위한 리스트 생성 (체스판 크기 l x l)
    visited = [[False] * l for _ in range(l)]

    # BFS 탐색을 위한 큐. (x, y 좌표와 이동 횟수)
    queue = deque([(start[0], start[1], 0)])

    # 출발 위치는 이미 방문한 것으로 처리
    visited[start[0]][start[1]] = True

    # 큐가 빌 때까지 BFS 반복
    while queue:
        x, y, count = queue.popleft()  # 현재 위치와 이동 횟수 가져오기

        # 나이트가 이동할 수 있는 8방향 탐색
        for dx, dy in moves:
            nx, ny = x + dx, y + dy  # 새로운 위치 계산

            # 체스판 내에 있는 유효한 좌표인지, 방문한 적이 없는지 확인
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                # 목표 위치에 도착한 경우, 이동 횟수 반환
                if (nx, ny) == end:
                    return count + 1

                # 방문 처리 후 큐에 추가 (다음 BFS 탐색을 위해)
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    return -1  # 목표 위치에 도달할 수 없으면 -1 반환

# 입력받기
T = int(input())
for tc in range(T):
    l = int(input())  # 체스판의 크기 입력
    start = tuple(map(int, input().split()))  # 나이트의 시작 위치 입력
    end = tuple(map(int, input().split()))  # 나이트의 목표 위치 입력
    
    # 메임함수 실행
    ans = bfs(l, start, end)
    
    # 결과 출력
    print(ans)