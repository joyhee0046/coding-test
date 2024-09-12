from collections import deque

def restore_road(road,N):

    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = deque([(0,0)])
    chek_time = [[9999 for _ in range(N)] for _ in range(N)]
    chek_time[0][0] = 0
    
    while queue:
        x, y = queue.popleft()

        for dir in dxy:
            nx = x + dir[0]
            ny = y + dir[1]

            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue

            new_time = chek_time[x][y] + road[nx][ny]

            if new_time < chek_time[nx][ny]:
                chek_time[nx][ny] = new_time
                queue.append([nx, ny])
    return chek_time[-1][-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    road = [list(map(int, input())) for _ in range(N)]
    
    ans = restore_road(road, N)

    print(f"#{tc} {ans}")