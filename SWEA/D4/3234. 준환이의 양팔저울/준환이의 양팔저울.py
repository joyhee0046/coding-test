# import sys
import math
# sys.stdin = open("sample_input (1).txt", "r")

"""
1. 왼쪽에 놓기/오른쪽에 놓기로 2^N (부분집합)
2. 올려놓은 후 추의 순서로 N! ( 순열 )

3. 왼쪽에 올려놓고 시작해도 된다. ( 오른쪽에 올려놓고 시작하면 안됨 ( 오른쪽이 더 무거울 수 없음 ) )
4. 
"""
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))


    def dfs(depth, l_sum, r_sum):
        global result

        # 오른쪽 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다 커지면 안됨
        if l_sum < r_sum:
            return

        # 이게 목표지만, 사실 이렇게 하면 시간초과이므로 아래 과정으로 백트래킹
        # if depth == N:
        #     result += 1
        #     return

        # 왼쪽 저울의 무게가 전체 무게의 절반이 넘는다면
        # 앞으로 뒤에 나올 모든 조합이 성립된다. (어떻게 놓든, 오른쪽에 더 무거워질 수도 없음 )
        # 나머지 조합의 시간복잡도는 문제에 나와있다. 2^N * N!

        if l_sum >= total_w / 2:
            result += (2 ** (N - depth)) * math.factorial(N - depth)
            return

        # 올려놓은 추를 제외하고, 나머지 추를 왼쪽에 놓는 경우/ 오른쪽에 놓는 경우 2가지를 dfs 한다.
        # 순열이기 때문에 N! 이고, 선택한 것을 제외한 나머지에서 선택
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = True
            dfs(depth + 1, l_sum + arr[i], r_sum)
            dfs(depth + 1, l_sum, r_sum + arr[i])
            visited[i] = False


    result = 0
    visited = [False] * N
    total_w = sum(arr)

    # 주어진 추를 하나씩 왼쪽에 올려놓고 시작을 함
    # 처음에는 어차피 오른쪽 저울에 못놓으므로
    # 왼쪽 저울에 올려놨다고 치고 dfs 진행
    for n in range(N):
        visited[n] = True
        """
        dfs 파라미터
        1. 재귀호출을 중단할 파라미터 => 해당 추를 선택하냐 안하냐를 가리키는 인덱스 (depth )
        2. 누적해서 가져가고 싶은 파라미터 => 왼쪽 저울의 무게, 오른쪽 저울의 무게  
        ( 문제의 조건을 계속해서 확인해야 하기 떄문에 )
        """
        dfs(1, arr[n], 0)
        visited[n] = False


    print(f"#{test_case} {result}")
