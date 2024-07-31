T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    burger_info = []
    for _ in range(N):
        burger_info.append(list(map(int, input().split())))
    burger_info.sort()

    result = set()
    def burger_comb(idx, sum_K, sum_T):

        if sum_K > L:
            return

        if idx == N:
            result.add(sum_T)
            return

        burger_comb(idx+1, sum_K, sum_T)

        burger_comb(idx+1, sum_K + burger_info[idx][1], sum_T + burger_info[idx][0])
        
        return result



    ans = max(burger_comb(0, 0, 0))

    print(f"#{tc} {ans}")