# import sys
# sys.stdin = open('sample_input (1).txt', 'r')


def create_num(op_list, idx, res):
    global max_num, min_num

    # 모든 숫자를 다 계산했다면
    if idx == N:
        max_num = max(max_num, res)  # 최대값 갱신
        min_num = min(min_num, res)  # 최소값 갱신
        return

    for op_idx, op_cnt in enumerate(op_list):
        # 남은 연산자가 없으면 넘어가기
        if op_cnt == 0:
            continue
        tmp_res = res
        if op_idx == 0:  # +
            tmp_res += numli[idx]
        elif op_idx == 1:  # -
            tmp_res -= numli[idx]
        elif op_idx == 2:  # *
            tmp_res *= numli[idx]
        elif op_idx == 3:  # /
            if numli[idx] == 0:  # 분모가 0인 경우는 계산 X
                return
            tmp_res = int(tmp_res / numli[idx])

        op_list[op_idx] -= 1
        create_num(op_list, idx + 1, tmp_res)
        op_list[op_idx] += 1

# 주어진 입력 받기
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    oper_li = list(map(int, input().split()))
    numli = list(map(int, input().split()))

    max_num = -100000000
    min_num = 100000000

    # 함수 실행
    create_num(oper_li, 1, numli[0])

    print(f"#{test_case} {max_num - min_num}")