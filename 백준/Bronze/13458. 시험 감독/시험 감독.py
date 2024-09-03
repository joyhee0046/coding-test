import math
# 주어진 입력 받기
N = int(input())
Ali = input()
Ali = list(map(int, Ali.split()))
B, C = map(int, input().split())

# 정답 더할 변수
ans = 0

# 감독할 학생 빼면서 감독 수 올리기
for i in range(N):
    Ali[i] -= B
    ans += 1
    if Ali[i] > 0:
        ans += math.ceil(Ali[i] / C)

print(ans)
