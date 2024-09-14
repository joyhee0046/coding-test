# import sys
# sys.stdin = open("sample_input.txt", "r")

#테스트 케이스 실행하며 입력 받기
T = int(input())
for tc in range(1, T+1):
    li = list(input())
    ans = 0   #조각 갯수
    branch = 0   #열린괄호 갯수 = 나무갯수
    for i in range(len(li)):
        # 열린괄호 다음이 닫힌괄호라면, elif를 고려해서 하나씩 조정해주기
        if li[i] == "(":
            if li[i+1] == ")":
                ans += branch
                branch += 1
                ans -= 1
            #열린괄호 다음이 닫힌괄호가 아니라면. 나무하나 추가
            else:
                branch +=1
        # 닫힌괄호는 나무하나 빼고 조각하나 추가
        elif li[i] == ")":
            branch -= 1
            ans += 1
    print(f"#{tc} {ans}")