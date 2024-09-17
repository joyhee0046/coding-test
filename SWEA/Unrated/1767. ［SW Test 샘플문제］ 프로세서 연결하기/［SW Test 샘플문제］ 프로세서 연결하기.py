# import sys
# sys.stdin = open('sample_input (2).txt', 'r')

from collections import defaultdict

# 전선 연결시 횟수 return
def connect(y, x, d):
    cnt = 0
    while True:
        # 사방 탐색
        y, x = y + dyx[d][0], x + dyx[d][1]
        # 보드를 벗어난다면 지나가기
        if not (0 <= y < N and 0 <= x < N):
            break
        # 빈자리가 아니라면 연결불가
        if board[y][x] != 0:
            return 0
        cnt += 1
    return cnt

# 전선에 맞게 맵을 변경
def change_board(y, x, connect_cnt, d, reverse=False):
    dy, dx = dyx[d]
    # 좌우 이동이라면
    if dx == 0:
        # 방문표시하며 진행
        for y_i in range(y + dy, y + dy * (connect_cnt + 1), dy):
            # 원복할때 동작
            if reverse:
                board[y_i][x] = 0
                continue
            board[y_i][x] = 2
    # 상하 이동이라면
    elif dy == 0:
        for x_i in range(x + dx, x + dx * (connect_cnt + 1), dx):
            if reverse:
                board[y][x_i] = 0
                continue
            board[y][x_i] = 2

def dfs(core_cnt=0, total_line_cnt=0, depth=0):
    global max_core, min_line
    # core를 모두 탐색한 경우
    if core_num == depth:
        # 연결한 개수가 최대 개수랑 같으면 최소 라인 수 갱신
        if max_core == core_cnt:
            min_line = min(min_line, total_line_cnt)
        # 연결한 개수가 가장 크다면 최소 라인수와 최대 개수 모두 갱신
        elif max_core < core_cnt:
            max_core = core_cnt
            min_line = total_line_cnt
        return
    # 코어 위치 받아오기
    y, x = cores[depth]
    # 사방 탐색
    for d in range(4):
        # 함수로 넘어가서 전선 수 가져오기
        line_cnt = connect(y, x, d)
        # 연결할 수 있다면 함수로 넘어가서 맵 변경
        if line_cnt:
            change_board(y, x, line_cnt, d)
        # 연결할 수 없다면 가지치기. 방향이 달라져도 같은 결과를 보임 -> 방문 확인
        else:
            if visited[core_cnt, total_line_cnt, depth, line_cnt]:
                continue
            visited[core_cnt, total_line_cnt, depth, line_cnt] = True
        # 다음 위치로 함수 실행
        dfs(core_cnt + bool(line_cnt), total_line_cnt + line_cnt, depth + 1)
        # 원복
        if line_cnt:
            change_board(y, x, line_cnt, d, True)

# 사방 탐색
dyx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 주어진 입력 받기
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 코어 위치 모으기
    cores = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if board[i][j] == 0:
                continue
            cores.append((i, j))
    core_num = len(cores)

    # 연결한 노드 수 갱신할 변수_가장 많이 연결하기
    max_core = 0
    # 연결에 사용한 라인 수 갱신할 변수_가장 조금 사용하기
    min_line = float('inf')
    # 방문처리할 배열 자동생성_사이즈를 안줘도 됨.
    visited = defaultdict(bool)
    # 메인 함수 실행
    dfs()
    # 정답 출력
    print(f"#{tc} {min_line}")