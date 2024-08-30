T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    group = [[i] for i in range(0, 1 + N)]
    for i in range(0, len(li), 2):
        for j in range(N+1):
            if li[i] in group[j]:
                for k in range(N+1):
                    if li[i+1] in group[k]:
                        if group[j] == group[k]:
                            break
                        group[j] += group[k]
                        group[k] = []
                        # print(group)
                        break
                break
            if li[i+1] in group[j]:
                for k in range(N+1):
                    if li[i] in group[k]:
                        if group[j] == group[k]:
                            break
                        group[j] += group[k]
                        group[k] = []
                        # print(group)
                        break
                break
    cnt = -1
    for i in range(N+1):
        if group[i]:
            cnt += 1
    print(f'#{tc} {cnt}')