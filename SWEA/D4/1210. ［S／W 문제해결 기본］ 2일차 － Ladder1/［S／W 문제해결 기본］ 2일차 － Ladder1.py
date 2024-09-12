# import sys
# sys.stdin = open('ladder_1_input.txt')

# # 문제대로 위에서부터 탐색
# # 아래, 좌, 우
# dxy = [[1, 0], [0, -1], [0, 1]]
# def search_leader(x, y):
#     # 원본을 훼손하지 않고, 방문체크할 수 있는 변수를 생성
#     visited = [[0] * 100 for _ in range(100)]
#     visited[x][y] = 1
#     # 맨 밑에 도달할 때까지 반복
#     while x != 99:
#         # 3방향으로 움직이는거 ( 아래, 좌, 우)
#         for dx, dy in dxy:
#             # 방향에 따라서 다음에 움직일 좌표를 구함
#             nx = x + dx
#             ny = y + dy
#
#             # 범위를 벗어난 경우에는 이건 옳지 않은 케이스
#             if nx < 0 or nx >= 100 or ny <0 or ny >= 100:
#                 continue
#
#             # 길이 아닌 경우
#             if not data[nx][ny]:
#                 continue
#
#             # 이미 방문한 경우
#             if visited[nx][ny]:
#                 continue
#
#             visited[x][y] = 1
#             x, y = nx, ny
#
#     # 마지막에 도달하고, 목적지가 2인 경우 (최종 목적지)
#     if data[x][y] == 2:
#         return True
#     return False
#
# for _ in range(1, 11):
#     tc = int(input())
#     result = -1  # 찾지 못하면 -1
#     data = [list(map(int, input().split())) for _ in range(100)]
#
#     # 출발점부터 시작을 해야 한다.
#     # 출발점은 0행에 있고, 1인 부분을 찾자
#     for j in range(100):
#         if data[0][j] == 0:
#             continue
#         # 출발점이라는 소리
#         if search_leader(0, j):
#             result = j
#             break
#     print(f"#{tc} {result}")
#


# 위, 좌, 우
# dxy = [[-1,0], [0, -1], [0, 1]]
dx = [-1, 0, 0]
dy = [0, -1, 1]
def search_leader(x, y):
    # 어차피 한 번에 될거니까 원본 훼손하자
    # 원본에서는 0이 못 지나가는 곳이고
    # 처음 시작하는 부분은 지나왔으니까 이제 못 지나가는 곳으로 변경
    data[x][y] = 0

    while x != 0:  # 제일 위로 올라갈 때까지 반복
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않고, 다음 사다리가 갈 수 있는 영역이면
            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny]:
                data[x][y] = 0
                x, y = nx, ny
    return y

for _ in range(1, 11):
    tc = int(input())
    result = -1  # 찾지 못하면 -1
    data = [list(map(int, input().split())) for _ in range(100)]

    # 도착점부터 시작하자
    # 도착점은 항상 99 번째 줄에 있겠죠
    for j in range(100):
        if data[99][j] == 2:
            result = search_leader(99, j)  # 어차피 답은 한 개거든요
            break
    print(f"#{tc} {result}")

##################################################################################
# input 파일 읽기
# import sys
# sys.stdin = open("input.txt", "r")

# # 테스트케이스 10번 반복
# for _ in range(10):
#     tc = int(input())
#     board = [list(map(int, input().split())) for _ in range(100)]
#     j = 0
#     # 최하단 왼쪽부터 목표지점인 2가 어느 위치에 있는지 확인. point에 2인 좌표 저장. x축 j에 저장
#     for i in range(100):
#         point = board[99][i]
#         if point == 2:
#             ans = i
#     # 목표지점에서 출발해서 위로 경로 탐색
#     j = ans
#     x = 98
#     board[x][j] = 0
#     while x != 0:
#         if board[x][j-1] == 1:
#             board[x][j-1] = 0
#             j -= 1
#         elif board[x][j+1] == 1:
#             board[x][j + 1] = 0
#             j += 1
#         elif board[x-1][j] == 1:
#             board[x - 1][j] = 0
#             x -= 1
#     print(f"#{tc} {j}")

#
#
# dxy = [[-1,0], [0, -1], [0, 1]]
#
# def search_leader(x, y):
#     data[x][y] = 0
#
#     while x != 0:
#         for i in range(len(dx)):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny]:
#                 data[x][y] = 0
#                 x, y = nx, ny
#     return y
#
# for _ in range(10):
#     tc = int(input())
#     result = -1  # 찾지 못하면 -1
#     data = [list(map(int, input().split())) for _ in range(100)]
#
#     # 도착점부터 시작하자
#     # 도착점은 항상 99 번째 줄에 있겠죠
#     for j in range(100):
#         if data[99][j] == 2:
#             result = search_leader(99, j)  # 어차피 답은 한 개거든요
#             break
#     print(f"#{tc} {result}")
