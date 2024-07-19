from itertools import combinations
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    if N >= 10 : 
        i = 2
    else :
        i = 1
    ans = 'No'
    while i<=9 :
        if N % i == 0 :
            if N//i >=10 :
                i+=1
            else :
                ans = 'Yes'
                break
        else :
            i +=1
    
    print(f"#{test_case} {ans}")
    