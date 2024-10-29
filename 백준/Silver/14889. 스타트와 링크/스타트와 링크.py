# 레시피 조합 찾기
def search_recipe(index_list, n):
    if n == 1:
        return [[i] for i in index_list]
    result = []
    for i in range(len(index_list) - 1):
        for j in search_recipe(index_list[i + 1:], n - 1):
            result.append([index_list[i]] + j)
    return result


n = int(input())
recipe = [list(map(int, input().split())) for _ in range(n)]
# 갱신할 목표 변수 만들기
min_diff = float('inf')
# 차집합을 만들기 위한 인덱스 리스트
index_set = set(range(n))
# 레시피 조합 찾아서 리스트로 저장
comb_list = [[0] + c for c in search_recipe(list(range(1, n)), n // 2 - 1)]
# 레시피 조합을 돌면서 시너지 점수 확인
for comb in comb_list:
    comb2 = list(index_set - set(comb))
    food1, food2 = 0, 0
    # 시너지 저장된 칸 돌면서 음식 점수 계산
    for i_idx, (i1, i2) in enumerate(zip(comb, comb2)):
        for j1, j2 in zip(comb[i_idx + 1:], comb2[i_idx + 1:]):
            # 음식 맛 계산하기
            food1 += recipe[i1][j1] + recipe[j1][i1]
            food2 += recipe[i2][j2] + recipe[j2][i2]
    # 두 집단 간의 차이가 가장 적도록 갱신
    min_diff = min(min_diff, abs(food1 - food2))

# 정답 출력
print(f"{min_diff}")