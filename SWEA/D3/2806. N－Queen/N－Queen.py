def dfs():
    if len(rdt) == N:
        global answer
        answer += 1
        return
 
    for i in range(N):
        if isSvb(i):
            rdt.append(i)
            dfs()
            rdt.pop()
    return
 
def isSvb(cand):
    for row,col in enumerate(rdt):
        if cand == col or len(rdt) - row == abs(cand - col):
            return False
    return True
 
 
tr = int(input())
for tc in range(1,1+tr):
    N = int(input())
    rdt = []
    answer = 0
    dfs()
    print(f"#{tc} {answer}")