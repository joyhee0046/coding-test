def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result .append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)
    return result

T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    li = list(map(int, input().split()))
    
    h= 0
    ans = []

    for i in range(1,N+1) : 
        result = comb(li, i)
        for j in range(0,len(result)) : 
            h= sum(result[j][:])
            if B <= h :
                ans.append(h)

    b = list(B for i in range(len(ans)))
    ans = [abs(ans[i] - b[i]) for i in range(len(ans))]

    print("#{} {}".format(test_case,min(ans)))
