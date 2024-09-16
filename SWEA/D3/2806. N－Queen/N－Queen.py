# import sys
# sys.stdin = open("sample_input.txt")
"""
row: 퀸을 놓을 행
col: 퀸을 놓을 열
"""
def is_valid_pos(row, col):
    # 현재 열에 다른 퀸이 있는지 검사
    for i in range(row):
        if board[i][col] == 1:
            return False

    """
    row = col = 2 인 경우 
    => for i, j in zip([2, 1, 0], [2, 1, 0]) 으로 풀어쓸 수 있고,
    zip 함수는 이 리스트 2개를 병렬로 묶기 때문에 
    => for i, j in [(2, 2), (1, 1), (0, 0)] 으로 변경되어 왼쪽 윗 대각선 순회를 돈다.
    왼 -> 오 에서 아래 대각선은 어차피 아직 퀸이 안 놓였기 때문에 검사할 필요 없음 
    """

    # 현재 위치의 왼쪽 윗 대각선에 다른 퀸이 있는지 검사
    # 아래는 검사할 필요가 없음
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    """
    row = col = 1 인 경우 
    => for i, j in zip([1, 0], [1, 2]) 으로 풀어쓸 수 있고,
    zip 함수는 이 리스트 2개를 병렬로 묶기 때문에 
    => for i, j in [(1, 1), (0, 2)] 으로 변경되어 오른쪽 윗 대각선 순회를 돈다.
    오 -> 왼 에서 아래 대각선은 어차피 아직 퀸이 안 놓였기 때문에 검사할 필요 없음 
    """
    # 현재 위치의 오른쪽 대각선에 다른 퀸이 있는지 검사
    # 아래는 검사할 필요가 없음
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    # 위의 모든 케이스에 해당하지 않으면 퀸을 놓을 수 있으므로 True
    return True

"""
row: 현재 퀸을 놓을 행
"""
def n_queens(row):
    global result

    # row가 보드의 크기에 도달했다는 것은
    # 모든 행에 퀸을 놓을 수 있는 경우
    if row == len(board):
        result += 1
        return

    # 현재 row 행에서 각 열에 대해 퀸을 놓을 수 있는지 검사
    for col in range(n):
        # 현재 위치(row, col)에 퀸을 놓을 수 있는 지 검사
        if is_valid_pos(row, col):
            board[row][col] = 1  # 현재 위치에 퀸을 놓음
            n_queens(row + 1)  # 다음 행으로 퀸을 놓을 수 있는 지 검사
            board[row][col] = 0  # 복구

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [[0] * n for _ in range(n)]  # 4*4 2차원 배열 생성
    result = 0

    # dfs 파라미터
    # 호출을 중단시킬 파라미터
    # => 각 행에 놓을 수 있는 지 확인하고, 마지막 행까지 간다면 전부 놓을 수 있는 상황 (idx)
    # 우리가 원하는 누적 결과값 => 딱히? 체스판? 근데 그냥 글로벌로 접근하자
    n_queens(0)
    print(f"#{tc} {result}")
