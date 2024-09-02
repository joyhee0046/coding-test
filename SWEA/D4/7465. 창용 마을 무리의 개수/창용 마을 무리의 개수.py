# import sys
# sys.stdin = open('s_input.txt', 'r')

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(M)]

    # 관계를 담을 리스트
    R_li = [i for i in range(N+1)]
    for a, b in li:
        if R_li[a] == R_li[b]:
            continue
        # 대표자 고르기
        res = min(R_li[a], R_li[b])
        # 대표자가 바뀌는지 확인, 바뀐다면 같은 대표자를 가진 모든 요소의 대표자 바꿔주기
        if R_li[a] != res:
            check = R_li[a]
            for i in range(N+1):
                if R_li[i] == check:
                    R_li[i] = res
        if R_li[b] != res:
            check = R_li[b]
            for i in range(N+1):
                if R_li[i] == check:
                    R_li[i] = res

    print(f'#{tc} {len(set(R_li))-1}')