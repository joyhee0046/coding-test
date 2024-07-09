T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    ans = []
    if N >= 50000 :
        ans.append(N//50000)
        N=N-(50000*(N//50000))
    else :
        ans.append(0)
    if N >= 10000 :
        ans.append(N//10000)
        N=N-(10000*(N//10000))
    else :
        ans.append(0)
    if N >= 5000 :
        ans.append(N//5000)
        N=N-(5000*(N//5000))
    else :
        ans.append(0)
    if N >= 1000 :
        ans.append(N//1000)
        N=N-(1000*(N//1000))
    else :
        ans.append(0)
    if N >= 500 :
        ans.append(N//500)
        N=N-(500*(N//500))
    else :
        ans.append(0)
    if N >= 100 :
        ans.append(N//100)
        N=N-(100*(N//100))
    else :
        ans.append(0)
    if N >= 50 :
        ans.append(N//50)
        N=N-(50*(N//50))
    else :
        ans.append(0)
    if N >= 10 :
        ans.append(N//10)
        N=N-(10*(N//10))
    else :
        ans.append(0)
    
    print("#{}".format(test_case))
    for i in range(8) :
        print(ans[i], end=" ")
    print("")