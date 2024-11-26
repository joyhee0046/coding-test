from collections import deque

def find_minimum_semesters(N, M, prerequisites):
    # 그래프 초기화
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    semester = [0] * (N + 1)

    # 그래프와 진입 차수 구성
    for A, B in prerequisites:
        graph[A].append(B)
        indegree[B] += 1

    # 위상 정렬을 위한 큐 초기화
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            semester[i] = 1  # 선수 과목이 없는 경우 1학기부터 시작

    # 위상 정렬 수행
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                semester[neighbor] = semester[current] + 1

    # 결과 반환
    return semester[1:]

# 입력
N, M = map(int, input().split())
prerequisites = [tuple(map(int, input().split())) for _ in range(M)]

# 처리 및 출력
result = find_minimum_semesters(N, M, prerequisites)
print(" ".join(map(str, result)))
