import heapq
dxy = [[1, 0], [0, 1], [0, -1], [-1, 0]]

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 줄기세포 자리 저장
    cell_set = set()
    # 확인할 줄기세포 넣을 리스트
    activate = []
    # 확인한 줄기세포 넣을 리스트
    tmp = []

    # 초기 입력값 (생명력, 세로좌표, 가로좌표, 생성후시간) 으로 구조화하여 힙큐 및 방문지에 추가
    for n in range(N):
        for m in range(M):
            # 좌표에 세포가 위치했다면
            if grid[n][m] != 0:
                # 생명력 x y 존재시간을 큐에 넣기. 최대힙으로 적용하기 위해서 생명력을 -로 변환
                heapq.heappush(activate, (-grid[n][m], n, m, 0))
                # 좌표 기록
                cell_set.add((n, m))

    for _ in range(K):  # K시간 동안
        while activate:  # 살아있는 세포들 모두 검토
            x, cx, cy, t = heapq.heappop(activate)
            # 최대힙을 넣기 위해서 음수로 넣었기 때문에, 뺄 때 다시 음수를 곱해서 변환
            x = -x

            # 세포가 생기고 지난 시간이 x보다 작다면 아직 비활성화상태.
            if t < x:
                # 시간의 흐름 반영해서 큐에 넣기
                heapq.heappush(tmp, (-x, cx, cy, t + 1))
                continue

            # 세포 시간이 2x보다 작다면 활성화중인 세포_비활성화는 컨티뉴당했으니까
            if t + 1 < 2 * x:
                # 시간의 흐름 반영해서 큐에 넣기
                heapq.heappush(tmp, (-x, cx, cy, t + 1))

            # 분열해야하는 경우라면
            if x == t:
                # 사방 탐색
                for dx, dy in dxy:
                    nx, ny = cx + dx, cy + dy
                    # 갈 자리에 다른 세포가 있다면 pass, 최대힙이라서 지나간게 무조건 큰 수
                    if (nx, ny) in cell_set: continue
                    # 아니라면 큐에 넣기
                    heapq.heappush(tmp, (-x, nx, ny, 0))
                    # 좌표도 추가해주기, 나중에 누가 들어오고싶어도 못들어오게
                    cell_set.add((nx, ny))
        # 확인할 세포 리스트 업데이트
        activate = tmp[:]
        # 지난 시간 세포 리스트 비우기
        tmp = []
    # 살아있는 줄기세포 수 구하기, 정답 출력
    ans = len(activate)
    print(f'#{tc} {ans}')