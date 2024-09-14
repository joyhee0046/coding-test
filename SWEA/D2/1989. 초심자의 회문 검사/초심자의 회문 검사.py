# import sys
# sys.stdin = open("input.txt", "r")

# #그냥 풀기
# T = int(input())
#
# for tc in range(1,T+1) :
#     li = list(input())
#     ans = 1
#     for i in range(len(li)//2) :
#         if li[i] == li[len(li)-i-1] :
#             pass
#         else :
#             ans = 0
#     print(f"#{tc} {ans}")

# #함수 이용
# def Palin(li) :
#     ans =li[::-1]
#     if li == ans :
#         return 1
#     else :
#         return 0
#
# T = int(input())
# for tc in range(1,T+1) :
#     li = list(input())
#     print(f"#{tc} {Palin(li)}")

#재귀함수 이용
def palin(li) :
    if len(li) < 2:
        return 1
    if li[0] != li[-1]:
        return 0
    return palin(li[1:-1])

T = int(input())
for tc in range(1,T+1) :
    li = list(input())
    print(f"#{tc} {palin(li)}")