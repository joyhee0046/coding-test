# import sys
# sys.stdin = open("sample_input.txt", 'r')

# 주어지는 입력받기
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    numli = list(map(int,input()))
    # 카드 개수 확인할 리스트
    checkli = [0 for i in  range(10)]

    # 숫자 리스트를 순회하며 카드 개수 올리기
    for turn in numli:
        checkli[turn] += 1

    # 가장 많은 카드 수를 큰 수부터 확인
    maxnum = max(checkli)
    for check in range(9,0,-1):
        if checkli[check] == maxnum:
            ans = [check, maxnum]
            break

    print(f"#{tc}", *ans)