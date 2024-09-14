# import sys
# sys.stdin = open("sample_input.txt", "r")

# #이동 함수 생성,
# def movement(idx, x, y, point):
#     dx = [0, -1, 0, 1]
#     dy = [1, 0, -1, 0]
#     point += board[x][y]
#     if idx == 6:
#         num_li.append(li)
#     for i in range(4):
#         x = x + dx[i]
#         y = y + dy[i]
#         if 0 <= x < 4 and 0 <= y < 4:
#             movement(idx+1, x, y, li)
#
# T = int(input())
# #테스트케이스 돌기
# for tc in range(1, T + 1):
#     board = [list(input().split()) for i in range(4)]
#     num_li = []
#     point = ''
#
#     #4*4배열의 모든 위치에서 시작해볼 수 있도록 반복
#     for x in range(4):
#         for y in range(4):
#             movement(0, x, y, point)
#
#     ans = set(num_li)
#     print('#{} {}'.format(tc, len(ans)))

#############################################
#############################################

def movement(idx, st_x, st_y, li):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    li += board[st_x][st_y]
    if idx == 6:
        num_li.append(li)
        return
    for i in range(4):
        x = st_x + dx[i]
        y = st_y + dy[i]
        if 0 <= x < 4 and 0 <= y < 4:
            movement(idx + 1, x, y, li)

T = int(input())
for tc in range(1, T + 1):
    board = [list(map(str, input().split())) for _ in range(4)]
    num_li = []
    li = ''
    for x in range(4):
        for y in range(4):
            movement(0, x, y, li)

    ans = set(num_li)
    print('#{} {}'.format(tc, len(ans)))