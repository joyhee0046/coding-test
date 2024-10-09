from collections import defaultdict

def dfs(node, depth):
    if depth == 4:
        return True

    visited[node] = True

    for this_n in graph[node]:
        if not visited[this_n]:
            if dfs(this_n, depth + 1):  # 다음 깊이로 이동
                return True

    # 회복
    visited[node] = False
    return False



N, M = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

visited = [False] * N

for i in range(N):
    if dfs(i, 0):  # 깊이 0에서 시작
        print(1)
        exit()

print(0)
