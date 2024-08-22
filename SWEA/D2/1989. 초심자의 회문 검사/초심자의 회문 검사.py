# import sys
# sys.stdin = open("input.txt", "r")

# 주어진 입력받기
T = int(input())
for tc in range(1, 1+T):
    words = list(input())

    ans = 1
    # 맨 앞과 맨 뒤가 같은지 확인
    for check in range(len(words)//2):
        if words[check] != words[-(check+1)]:
            ans = 0
            break

    # 정답 출력
    print(f"#{tc} {ans}")