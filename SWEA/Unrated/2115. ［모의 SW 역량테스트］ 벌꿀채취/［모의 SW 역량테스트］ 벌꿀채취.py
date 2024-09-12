from itertools import combinations
 
T = int(input())
for tc in range(1, T+1):
    n, m, c = list(map(int, input().split()))
 
    maps = [list(map(int, input().split())) for _ in range(n)]
 
    # 각 구역의 최대 수익을 계산하는 함수
    def calculate_profit(honey):
        max_profit = 0
        # 가능한 모든 조합을 구해 이익을 계산
        for i in range(1, len(honey) + 1):
            for comb in combinations(honey, i):
                if sum(comb) <= c:
                    max_profit = max(max_profit, sum([x ** 2 for x in comb]))
        return max_profit
 
    # 각 줄에서 선택 가능한 벌통의 최대 수익 계산
    profits = []
    for i in range(n):
        for j in range(n - m + 1):  # 선택할 벌통의 범위 설정
            honey = maps[i][j:j + m]  # m개의 벌통 선택
            profit = calculate_profit(honey)
            profits.append((profit, (i, j, j + m - 1)))  # 수익과 위치 저장
 
    max_total_profit = 0
    # 두 벌통이 겹치지 않도록 조합을 선택
    for (profit1, (x1, y1_start, y1_end)), (profit2, (x2, y2_start, y2_end)) in combinations(profits, 2):
        if x1 != x2 or y1_end < y2_start:  # 다른 줄에 있거나, 같은 줄이라도 겹치지 않을 때
            max_total_profit = max(max_total_profit, profit1 + profit2)
 
    print(f'#{tc} {max_total_profit}')