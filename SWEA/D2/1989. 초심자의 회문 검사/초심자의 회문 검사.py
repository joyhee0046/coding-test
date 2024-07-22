def palin(li) :
    if len(li) < 2:
        return 1
    if li[0] != li[-1]:
        return 0
    return palin(li[1:-1])

T = int(input())
for tc in range(1,T+1) :
    li = list(input())
    print(f"#{tc} {palin(li)}")