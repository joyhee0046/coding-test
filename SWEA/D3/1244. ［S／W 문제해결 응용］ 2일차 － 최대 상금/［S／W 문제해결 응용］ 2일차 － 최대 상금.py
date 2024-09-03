# import sys
# sys.stdin = open('input.txt','r')

def max_prize(borad, num):
    global check_borad
    # 변경횟수가 0번 남을때까지 반복
    if num == 0:
        # 더 큰 값 고르기
        check_borad = max(check_borad, int(''.join(map(str, borad))))
        return check_borad

    for i in range(n):
        # i랑 j조합 만들기
        for j in range(i + 1, n):
            # 맘대로 수정할 임시 보드 만들기
            tmp_borad = borad[:]
            # i, j조합으로 자리 바꾸기
            tmp_borad[i], tmp_borad[j] = tmp_borad[j], tmp_borad[i]
            # 바꿔준 위치와 남은 횟수가 이미 했던 검사면 지나가기
            if (num, tmp_borad) not in visited:
                # 재귀로 다음 카드 바꾸기.
                max_prize(tmp_borad, num - 1)
                # visited에 남은 교환횟수랑 지금 값 저장_ 중복 작업 방지
                visited.append((num, tmp_borad))

# 주어진 입력 받기
T = int(input())
for tc in range(1, 1 + T):
    borad, num = map(str, input().split())
    borad = list(int(i) for i in borad)
    num = int(num)
    n = len(borad)

    check_borad = 0
    visited = []

    max_prize(borad, num)  # 함수 호출, 카드리스트와 교환횟수

    # 정답 출력
    print(f"#{tc} {check_borad}")