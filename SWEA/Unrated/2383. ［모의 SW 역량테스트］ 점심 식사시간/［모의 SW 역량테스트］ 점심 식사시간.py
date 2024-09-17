# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque


def get_dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


"""
1) 사람들을 계산으로 분배하기 ( 조합 => dfs ) , combination 상관없다 .
2) 분배된 사람들을 대상으로 이제 계단에서 내려보내기 
"""
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    MAX_PEOPLE_ON_STAIRS = 3
    min_time = 999999

    # 문제에서 주어진 입력값을 돌면서 , 사람들의 위치와 계단의 위치를 파악하자
    people_list = []  # 사람들의 위치를 저장
    stair_list = []  # 계단의 위치를 저장

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0: continue  # 빈 공간
            if maps[i][j] == 1: people_list.append([i, j])  # 사람들의 위치 추가
            else:
                stair_list.append([i, j, maps[i][j]])  # 계단의 위치와 길이 추가

    def dfs(idx, a_dist_list, b_dist_list):
        global min_time

        # dfs가 진행될 때마다 a 계단, b 계단에 사람들은 계속해서 도착하고 있다.
        # a 계단에 도착한 사람들 중에서 가장 늦은 사람 => 계단을 내려가는 시간이
        # 여태까지 갱신된 최소로 걸리는 시간보다 늦으면, 사실 내려가는 과정도 진행할 필요가 없습니다.
        # 대기하고 있는 사람이 존재하는데, 대기 하는 사람 목록에서 가장 늦은 친구 + 계단의 길이가
        # 최소값보다 크면 가지치기
        if a_dist_list and min_time <= max(a_dist_list) + stair_list[0][2]: return
        if b_dist_list and min_time <= max(b_dist_list) + stair_list[1][2]: return

        # 이번에 선택할 사람의 인덱스가 총 사람의 수와 같아지면, 이제 계단으로 내려보내는 로직을 실행
        if idx == len(people_list):
            # 사람들이 각 계단에 알맞게 도착을 했다.
            # 계단을 내려가는 로직을 작성

            # 계단의 공간을 의미하는 리스트를 하나 만든다.
            a_stair_on_list = [0] * MAX_PEOPLE_ON_STAIRS
            b_stair_on_list = [0] * MAX_PEOPLE_ON_STAIRS

            # 각 계단에 도착한 시간
            # 먼저 도착한 순서대로 정렬을 해준다.
            a_dist_list.sort()
            b_dist_list.sort()

            # 먼저 온 사람부터 추출하기 위해서 deque 활용 ( 데이터 앞에서 뺄거니까)
            a_queue = deque(a_dist_list)
            b_queue = deque(b_dist_list)

            # 시간을 앞으로 1초씩 늘려나갈거니까 ,초기값 = 0
            t = 0

            while True:
                # 시간이 흐르면서.. 계단에 올라가있는 사람들의 시간을 1초씩 줄인다.
                # 이 과정을 통해서 초가 0이 된 사람은 게단을 다 내려가겠죠 ?
                # 그러면 계단에 공간이 생깁니다.
                for idx in range(MAX_PEOPLE_ON_STAIRS):  # 0, 1, 2
                    if a_stair_on_list[idx] != 0:
                        a_stair_on_list[idx] -= 1

                for idx in range(MAX_PEOPLE_ON_STAIRS):  # 0, 1, 2
                    if b_stair_on_list[idx] != 0:
                        b_stair_on_list[idx] -= 1
                # 계단 입구에서 기다리고 있는 친구들을 계단을 보내봅시다.

                for stair_idx in range(MAX_PEOPLE_ON_STAIRS):  # 0, 1, 2
                    # 계단에 공간이 존재해야해요,
                    # a 입구에서 기다리는 사람이 있어야해요
                    # 그 사람들이 현재 시간에 적절하게 와있어야 한다.
                    # 현재 t=1 이면 , 4초에 도착한 사람은 아직은 계단에 내려가면 안된다
                    # 이미 도착해 있어야한다.
                    if a_queue and a_queue[0] <= t and a_stair_on_list[stair_idx] == 0:
                        pop_data = a_queue.popleft()

                        # 대신 동일한 시간에 동일하게 도착한 사람을 넣을 경우네느 바로 못들어간다.
                        if pop_data == t:
                            a_stair_on_list[stair_idx] = stair_list[0][2] + 1
                        else:
                            # 비어있는 공간에 넣는데, 계단의 길이를 넣어야한다.
                            a_stair_on_list[stair_idx] = stair_list[0][2]

                    if b_queue and b_queue[0] <= t and b_stair_on_list[stair_idx] == 0:
                        pop_data = b_queue.popleft()

                        # 대신 동일한 시간에 동일하게 도착한 사람을 넣을 경우네느 바로 못들어간다.
                        if pop_data == t:
                            b_stair_on_list[stair_idx] = stair_list[1][2] + 1
                        else:
                            # 비어있는 공간에 넣는데, 계단의 길이를 넣어야한다.
                            b_stair_on_list[stair_idx] = stair_list[1][2]

                # 계단에서 내려가는 친구도 없고, 계단에서 기다리는 친구도 없고, 다 내려갔으므로 종료 !
                if (not a_queue and not b_queue and
                        sum(a_stair_on_list) == 0 and sum(b_stair_on_list) == 0):
                    break
                t += 1

                # 이미 이전에 최소값이 갱신된 적이 있따?
                if min_time <= t:
                    return

            min_time = min(min_time, t)
            return

        # idx에 해당하는 사람들을 a로 보낼지, b로 보낼지 고민해보자.
        # 선택한 사람이 해당 계단까지 가는데 걸리는 거리(시간)
        # 우리가 선택한 사람의 위치와 보내려는 계단의 위치
        # 이 친구를 a 계단에 보낼거다.
        a_dist = get_dis(people_list[idx], stair_list[0][:2])
        dfs(idx + 1, a_dist_list + [a_dist], b_dist_list)

        b_dist = get_dis(people_list[idx], stair_list[1][:2])
        dfs(idx + 1, a_dist_list, b_dist_list + [b_dist])


    # 사람들을 계단으로 분배시키는 역할을 하는 dfs
    # 파라미터
    # 1. 재귀호출을 종료하는 조건 => 계단으로 분배한 사람의 수 (depth)
    # 2. 누적해서 가져가고 싶은 값,
    # => a 계단에 도착한 사람 리스트(사람마다 도착하는 데 걸리는 시간), b 계단에 도착한 사람 리스트
    dfs(0, [], [])

    print(f"#{test_case} {min_time}")
