import itertools

# 델타 탐색 (상, 하, 좌, 우)
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 전역 변수 정의
N = W = H = result = 0
matrix = []

def solution():
    global N, W, H, result, matrix
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    T = int(input())  # 테스트 케이스 수
    
    for test_case in range(1, T + 1):
        N, W, H = map(int, input().split())
        matrix = [list(map(int, input().split())) for _ in range(H)]  # 벽돌 상태 입력
        result = W * H + 1  # 최대 값 초기화
        backup = [arr[:] for arr in matrix]  # 초기 상태 백업

        # 가능한 구슬 던지기 순열 생성
        items = [i for i in range(W)]
        perms = list(itertools.product(items, repeat=N))  # 구슬 던지기 순열

        for p in perms:
            matrix = [arr[:] for arr in backup]  # 매번 초기화
            for col in p:
                target(col)  # 구슬 던지기
                organize()    # 벽돌 떨어뜨리기
            bricks = count_all_bricks()  # 남은 벽돌 개수 카운트

            if bricks < result:
                result = bricks  # 최솟값 업데이트

        print(f'#{test_case} {result}')

# 구슬이 던져지는 열에서 가장 위의 벽돌 찾기
def target(c):
    for r in range(H):
        if matrix[r][c] > 0:  # 벽돌이 있을 때
            bomb(r, c, matrix[r][c])  # 벽돌 부수기
            return

# 벽돌을 부수는 함수
def bomb(r, c, limit):
    matrix[r][c] = 0  # 해당 벽돌을 부수기
    for i in range(4):  # 4방향 탐색
        nr, nc = r, c
        for count in range(1, limit):  # limit 만큼 벽돌을 부수기
            nr, nc = nr + dxy[i][0], nc + dxy[i][1]
            if not range_validation(nr, nc):  # 범위 초과시 종료
                break
            if matrix[nr][nc] > 0:  # 벽돌이 있으면 부수기
                bomb(nr, nc, matrix[nr][nc])  # 재귀적으로 부수기

# 벽돌이 떨어지도록 하는 함수
def organize():
    for c in range(W):
        for r in range(H-1, -1, -1):  # 아래에서 위로
            if matrix[r][c] > 0:  # 벽돌이 있으면
                go_down(r, c)

# 벽돌을 아래로 떨어뜨리는 함수
def go_down(r, c):
    if not range_validation(r+1, c):  # 범위 벗어나면 종료
        return
    if matrix[r+1][c] == 0:  # 아래가 비어있으면
        matrix[r+1][c] = matrix[r][c]
        matrix[r][c] = 0
        go_down(r+1, c)  # 재귀적으로 내려가면서 처리

# 범위 검사 함수
def range_validation(r, c):
    if 0 <= r < H and 0 <= c < W:
        return True
    return False

# 남아있는 벽돌의 개수를 세는 함수
def count_all_bricks():
    count = 0
    for r in range(H):
        for c in range(W):
            if matrix[r][c] > 0:
                count += 1
    return count

# 프로그램 실행
solution()
