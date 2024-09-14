# import sys
# sys.stdin = open("input.txt", "r")

# 그냥 풀기
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input())) for _ in range(N)]
    j = N//2
    k = N//2+1
    ans = 0
    for i in range(N):
        for u in range(j, k):
            ans = ans + li[i][u]
        if i >= N//2:
            j += 1
            k -= 1
        else:
            j -= 1
            k += 1

    print(f'#{tc} {ans}')