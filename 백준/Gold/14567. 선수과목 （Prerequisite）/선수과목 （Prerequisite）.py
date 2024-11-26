from collections import deque

def find_minimum_semesters(N, M, prerequisites):
    # 그래프를 나타내기 위한 인접 리스트
    graph = [[] for _ in range(N + 1)]  # 각 정점마다 연결된 정점들 리스트
    indegree = [0] * (N + 1)  # 각 정점의 진입 차수 (선수 과목 개수)
    semester = [0] * (N + 1)  # 각 정점의 최소 이수 학기

    # 1. 그래프 및 진입 차수 초기화
    for A, B in prerequisites:
        graph[A].append(B)  # A -> B 방향 간선 추가 (A를 들어야 B를 들을 수 있음)
        indegree[B] += 1    # B번 과목의 진입 차수 증가

    # 2. 진입 차수가 0인 과목(선수 과목 없이 바로 들을 수 있는 과목)을 큐에 삽입
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:  # 선수 과목이 없는 경우
            queue.append(i)   # 큐에 추가
            semester[i] = 1   # 선수 과목이 없으므로 1학기부터 시작 가능

    # 3. 위상 정렬 수행
    while queue:
        current = queue.popleft()  # 큐에서 정점을 하나 꺼냄
        for neighbor in graph[current]:  # 현재 과목의 후속 과목 탐색
            indegree[neighbor] -= 1  # 후속 과목의 진입 차수를 감소
            if indegree[neighbor] == 0:  # 진입 차수가 0이 된 경우
                queue.append(neighbor)  # 큐에 추가
                # 후속 과목의 학기는 현재 과목의 학기 + 1
                semester[neighbor] = semester[current] + 1

    # 4. 결과 반환
    # 1번 과목부터 N번 과목까지 각 과목의 최소 학기를 반환
    return semester[1:]

# 입력 받기
N, M = map(int, input().split())  # 과목 수(N), 선수 조건 수(M)
prerequisites = [tuple(map(int, input().split())) for _ in range(M)]  # 선수 조건 입력

# 최소 학기 계산
result = find_minimum_semesters(N, M, prerequisites)

# 결과 출력
print(" ".join(map(str, result)))  # 각 과목의 최소 학기를 공백으로 구분하여 출력
