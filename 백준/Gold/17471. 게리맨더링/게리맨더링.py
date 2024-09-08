import itertools, collections

def bfs(graph, comb, visited, p_sum):
    que = collections.deque([comb[0]])
    visited.add(comb[0])
    while que:
        node = que.popleft()
        p_sum += p_num[node]
        for n_node in graph[node]:
            if n_node in visited:
                continue
            if n_node not in comb:
                continue
            que.append(n_node)
            visited.add(n_node)
    if len(comb) == len(visited):
        return p_sum
    return -1


N = int(input())
p_num = [0] + list(map(int, input().split()))



comb = []
for i in range(1, N):
    comb.extend(list(itertools.combinations([j for j in range(1,N+1)], i)))
# print(comb)

min_p = 9999999999

graph = {}
for i in range(1, N+1):
    x, *y = map(int, input().split())
    graph[i] = y
# print(graph)

total_li = set([j for j in range(1, N + 1)])
for j in comb:
    visited = set()
    # print(j)
    p_sum = 0
    ans1 = bfs(graph, j, visited, p_sum)
    if ans1 == -1:
        continue
    k = list(total_li - set(j))
    visited = set()
    # print(j)
    p1_sum = 0
    ans2 = bfs(graph, k, visited, p1_sum)
    if ans2 == -1:
        continue
    min_p = min(min_p, abs(ans1 - ans2))

if min_p == 9999999999:
    min_p = -1
print(min_p)