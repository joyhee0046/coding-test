from itertools import combinations

# 입력 받기
N, M = map(int, input().split())  # N은 도시의 크기(N x N), M은 최대 남길 치킨집 수
city = [list(map(int, input().split())) for _ in range(N)]  # 도시의 정보를 N x N 리스트로 입력 받음

# 집과 치킨집 위치를 저장할 리스트
houses = []  # 집의 위치를 저장할 리스트
chicken_shops = []  # 치킨집의 위치를 저장할 리스트

# 도시의 각 칸을 확인하여 집과 치킨집의 위치를 구분하여 저장
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:  # 해당 칸이 집(1)인 경우
            houses.append((r, c))  # houses 리스트에 (r, c) 좌표 추가
        elif city[r][c] == 2:  # 해당 칸이 치킨집(2)인 경우
            chicken_shops.append((r, c))  # chicken_shops 리스트에 (r, c) 좌표 추가

# 최소 도시 치킨 거리를 매우 큰 값으로 초기화
min_city_chicken_distance = float('inf')  # 최소값을 구하기 위해 초기값을 무한대로 설정

# 치킨집 중 M개를 선택하는 모든 조합에 대해 최소 도시 치킨 거리 계산
for chicken_comb in combinations(chicken_shops, M):  # 모든 치킨집 중 M개를 선택하는 조합 생성
    total_distance = 0  # 현재 선택된 치킨집 조합에 대한 총 도시 치킨 거리를 계산할 변수 초기화

    # 각 집에 대해 가장 가까운 치킨집과의 거리를 구함
    for hr, hc in houses:  # 모든 집의 위치를 하나씩 가져와서
        min_distance = float('inf')  # 각 집에서 가장 가까운 치킨집과의 거리를 무한대로 초기화
        for cr, cc in chicken_comb:  # 선택된 M개의 치킨집 중 하나씩 확인
            # 현재 집과 치킨집 간의 거리를 계산 (맨해튼 거리 공식 사용)
            distance = abs(hr - cr) + abs(hc - cc)
            # 가장 가까운 치킨집과의 거리 갱신
            if distance < min_distance:
                min_distance = distance
        # 현재 집의 치킨 거리를 총 치킨 거리(total_distance)에 더함
        total_distance += min_distance

    # 현재 선택된 치킨집 조합에 대한 도시 치킨 거리가 최소값인지 확인
    if total_distance < min_city_chicken_distance:
        min_city_chicken_distance = total_distance  # 최소값 갱신

# 결과 출력
print(min_city_chicken_distance)  # 모든 가능한 치킨집 조합 중에서 도시 치킨 거리가 최소인 값을 출력
