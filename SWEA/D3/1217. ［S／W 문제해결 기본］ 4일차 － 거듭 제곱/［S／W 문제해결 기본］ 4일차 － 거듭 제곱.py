# import sys
# sys.stdin = open("input.txt", "r")

# #그냥 풀기
# for i in range(10) :
#     tc = int(input())
#     N, M = map(int, input().split())
#     ans = 1
#     for i in range(M) :
#         ans = ans*N
#
#     print(f"#{tc} {ans}")
#

#재귀로 풀기
def power(n, m):
    if m <= 0:
        return 1
    else:
        return n * power(n, m - 1)

for i in range(10):
    tc = int(input())
    N, M = map(int, input().split())

    print(f"#{tc} {power(N, M)}")