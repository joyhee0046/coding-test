def dfs(string, cnt_list):  # 시작 문자열과 남은 문자열 개수 리스트
    global result
    # 이미 결과를 찾은 경우에는 함수를 바로 종료
    if result:
        return
    # 01과 10의 개수 차이는 2개 이상이 될 수 없다. 조건 못 맞추면 얼리리턴
    if abs(cnt_list[1] - cnt_list[2]) > 1:
        return
    # 모든 문자를 다 사용해서, 결과를 찾은 경우 끝내기
    if sum(cnt_list) == 0:
        result = string
        return

    # 남은 문자열 조정하며 DFS 재귀 돌리기
    if string[-1] == '0':
        # 00을 이어서 시작
        if cnt_list[0] > 0:
            cnt_list[0] -= 1
            dfs(string + '0', cnt_list)
            cnt_list[0] += 1
        # 01을 이어서 시작
        if cnt_list[1] > 0:
            cnt_list[1] -= 1
            dfs(string + '1', cnt_list)
            cnt_list[1] += 1
    # 마지막이 1로 끝났다면
    if string[-1] == '1':
        # 10으로 이어서 시작
        if cnt_list[2] > 0:
            cnt_list[2] -= 1
            dfs(string + '0', cnt_list)
            cnt_list[2] += 1
        # 11로 이어서 시작
        if cnt_list[3] > 0:
            cnt_list[3] -= 1
            dfs(string + '1', cnt_list)
            cnt_list[3] += 1

# 주어진 입력 모두 받기
binary_types = ['00', '01', '10', '11']
T = int(input())
for test_case in range(1, T + 1):
    binary_cnt_list = list(map(int, input().split()))

    # 문자열 담을 변수
    result = ''
    # binary_types에 대해서 모두 DFS를 실행
    for idx in range(4):
        # 남은 수가 있으면 시작
        if binary_cnt_list[idx] > 0:
            # 사용할거니까 1 빼고 함수실행
            binary_cnt_list[idx] -= 1
            dfs(binary_types[idx], binary_cnt_list)
            # 함수 끝났으면 원복
            binary_cnt_list[idx] += 1
        # 이미 결과를 도출했다면 for loop 중단
        if result:
            break
    # 결과 출력
    print(f"#{test_case} {result or 'impossible'}")