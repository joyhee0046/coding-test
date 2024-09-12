# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

def find_road(maze, st_x, st_y):

    maze_check = [[-1] * 16 for _ in range(16)]
    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    que = deque([(st_x, st_y)])
    maze_check[st_x][st_y] = 0

    while que:
        x, y = que.popleft()
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 > nx or nx >= 16 or 0 > ny or ny >= 16:
                continue
            if maze[nx][ny] == 1:
                continue
            if maze_check[nx][ny] != -1:
                continue

            que.append((nx,ny))
            maze_check[nx][ny] = 0

            if maze[nx][ny] == 3:
                return 1
    return 0


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                st_x, st_y = i, j

    ans = find_road(maze, st_x, st_y)

    print(f"#{tc} {ans}")