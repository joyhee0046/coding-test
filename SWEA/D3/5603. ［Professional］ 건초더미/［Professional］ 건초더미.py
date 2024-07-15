T = int(input())

for tc in range(1,T+1) :
    N = int(input())
    dum = []
    for i in range(N) :
        dum.append(int(input()))
    avg = sum(dum)/len(dum)
    ans = []
    for i in range(N) :
        ans.append(abs(dum[i]-avg))
    print(f"#{tc} {int(sum(ans)/2)}")