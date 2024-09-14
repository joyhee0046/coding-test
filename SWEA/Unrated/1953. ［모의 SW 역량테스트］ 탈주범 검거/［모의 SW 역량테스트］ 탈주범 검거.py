# import sys
# sys.stdin = open("sample_input.txt", 'r')

# 사방으로 움직일 xy짝꿍
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 구조물 종류
structure = {1: [0, 1, 2, 3], 2: [0, 2], 3: [1, 3], 4: [0, 1], 5: [1, 2], 6: [2, 3], 7: [3, 0]}

# 입력받기
T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    # 확인했는지 체크할 배열
    tunnel_check = [[0] * M for _ in range(N)]
    # 큐에 시작점 넣기
    check_point = [(R, C)]
    # 시작점 확인했다고 체크
    tunnel_check[R][C] = 1

    # 확인할 지점이 남아있다면 계속 반복
    while check_point:
        x, y = check_point.pop(0)
        # 
        if tunnel_check[x][y] >= L:
            break
        else:
            # 구조물 경로만큼 반복
            for i in structure[tunnel[x][y]]:
                nx = x + dx[i]
                ny = y + dy[i]
                # 구조물을 벗어나는지 확인
                if 0 > nx or nx >= N or 0 > ny or ny >= M:
                    continue
                # 확인한 자리인지, 길이 없는지 확인
                if tunnel_check[nx][ny] != 0 or tunnel[nx][ny] == 0:
                    continue
                # ??????
                if (i + 2) % 4 in structure[tunnel[nx][ny]]:
                    check_point.append((nx, ny))
                    tunnel_check[nx][ny] = tunnel_check[x][y] + 1
    # 칸 수 셀 변수
    result = 0

    # 전체를 돌면서 확인
    for i in range(N):
        for j in range(M):
            # 몇 칸 이동할 수 있는지 확인
            if tunnel_check[i][j] > 0:
                result += 1
    print(f'#{tc} {result}')