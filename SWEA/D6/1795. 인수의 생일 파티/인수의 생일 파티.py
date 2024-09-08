# import sys
# sys.stdin = open('input (2).txt', 'r')

import math, heapq

def dijkstra(graph, start):
    # start로 부터의 거리 값을 저장하기 위함
    distances = {node: INF for node in graph}
    # 시작 값은 0이어야 함
    distances[start] = 0
    queue = []
    # 시작 노드부터 탐색 시작 하기 위함.
    heapq.heappush(queue, [distances[start], start])

    # queue에 남아 있는 노드가 없으면 끝
    while queue:
        # heap에서 탐색 할 노드, 거리를 가져옴.
        current_distance, current_destination = heapq.heappop(queue)
        # 기존에 있는 거리보다 길다면, 볼 필요도 없음
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            # 해당 노드를 거쳐 갈 때 거리
            distance = current_distance + new_distance
            # 알고 있는 거리 보다 작으면 갱신
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                # 다음 인접 거리를 계산 하기 위해 큐에 삽입
                heapq.heappush(queue, [distance, new_destination])
    return distances

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    graph = {}
    graph_rev = {}
    for i in range(M):
        x, y, c = map(int, input().split())
        if x not in graph:
            graph[x] = {}
        graph[x][y] = c
        if y not in graph_rev:
            graph_rev[y] = {}
        graph_rev[y][x] = c
    # print(graph)
    # print(graph_rev)

    INF = math.inf

    from_x = dijkstra(graph, X)
    # print('x에서 가는 그래프', from_x)
    to_x = dijkstra(graph_rev, X)
    # print('x로 가는 그래프', to_x)

    ans = 0
    for i in range(1, N+1):
        ans = max(ans, from_x[i] + to_x[i])
    print(f'#{tc} {ans}')