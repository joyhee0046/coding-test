# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    li_A = list(map(int, input().split()))

    ans_cnt = 0

    def dfs(idx, sum_ans):
        global ans_cnt

        if sum_ans > K:
            return

        if sum_ans == K:
            ans_cnt+=1
            return

        if idx == N:
            return

        dfs(idx + 1, sum_ans + li_A[idx])
        dfs(idx + 1, sum_ans)


    dfs(0, 0)

    print(f"#{tc} {ans_cnt}")




# import sys
# sys.stdin = open("sample_input.txt", "r")
#
#
# T = int(input())
# for tc in range(1, 1+T):
#     N, K = map(int, input().split())
#     li_A = list(map(int, input().split()))
#
#     li_check = [0] * N
#     ans_cnt = 0
#     sum_ans = 0
#
#     ### 지금은 순열인데..?;;
#     def dfs(idx, sum_ans):
#         global ans_cnt
#
#         if sum_ans > K:
#             return
#
#         if sum_ans == K:
#             ans_cnt += 1
#             return
#
#         if idx == N:
#             return
#
#         for i in range(N):
#             if li_check[i] == 1: continue
#             li_check[i] = 1
#             dfs(idx+1, sum_ans + li_A[i])
#
#             li_check[i] = 0
#
#
#     dfs(0, 0)
#
#     print(ans_cnt)


    # for i in range(N):
    #     li_check[i] = 1
    #     sum_ans += li_A[i]
    #
    #         li_check[i] = 0
    #         sum_ans -= li_A[i]
    #         break







    # def comb(li_A, n):  # arr 배열에서 n개의 요소를 선택
    #     global ans_cnt, K
    #     result = 0  # 결과를 저장할 리스트
    #     if n == 1:  # 선택할 요소의 수가 1인 경우, 각 요소를 리스트로 감싸서 반환
    #         for i in li_A:
    #             if i == K: ans_cnt += 1
    #         return ans_cnt
    #     for i in range(len(li_A)):  # 배열의 각 요소에 대해 반복
    #         elem = li_A[i]  # 현재 요소를 선택
    #         if result + elem < K:
    #             for rest in comb(li_A[i + 1:], n - 1):
    #
    #                 result += [elem] + rest  # 현재 선택한 요소와 재귀 호출을 통해 얻은 조합을 합침
    #         else :
    #             continue
    #     return result  # 최종 조합 결과 반환
    #
    # for i in range(1, N+1):
    #     print(comb(li_A, i))



#
# import itertools
#
# T = int(input())
# for tc in range(1, 1+T):
#     N, K = map(int, input().split())
#     li_A = list(map(int, input().split()))
#     ans_cnt = 0
#
#     for i in range(1, N+1):
#         comb = list(itertools.combinations(li_A, i))
#         for j in range(len(comb)):
#             if sum(comb[j]) == K:
#                 ans_cnt += 1
#         print(comb)
#     print(f"#{tc} {ans_cnt}")
#

#
# import itertools
#
# T = int(input())
# for tc in range(1, 1+T):
#     N, K = map(int,input().split())
#     li_A = list(map(int,input().split()))
#     ans_cnt = 0
#
#     if K in li_A:
#         for i in range(N):
#             if li_A[i] == K:
#                 ans_cnt += 1
#
#     for i in range(2, N+1):
#         comb = list(itertools.combinations(li_A, i))
#         for j in range(len(comb)):
#             if sum(comb[j]) == K:
#                 ans_cnt += 1
#     print(f"#{tc} {ans_cnt}")
#
