T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    li_A = list(map(int, input().split()))
 
    li_check = [0] * N
    ans_cnt = 0
    sum_ans = 0
 
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