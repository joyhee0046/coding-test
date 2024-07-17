from itertools import combinations
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    li = list(map(int, input().split()) )
    cbli=[]
    adli=[]
    for i in combinations( li , 3) :
        cbli.append(i)
    for i in range(len(cbli)):
        adli.append(sum(cbli[i][:]))
    set_adli=set(adli)
    adli = list(set_adli)
    adli.sort(reverse=True)
    print(f"#{test_case} {adli[4]}")