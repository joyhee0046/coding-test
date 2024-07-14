import math
T = int(input())
for tc in range(1,T+1) :

    li = list(input())
    N = math.ceil(len(li)/2)
    li_copy = list(li)
    ans = []
    while True :
        for i in range(len(li)) :
            po = li[i]
            if po in li_copy :
                li_copy.remove(po)
                if po in li_copy : 
                    li_copy.remove(po)
                else :
                    li_copy.append(po)
                    ans.append(po)
        break
    if ans == [] :
        print(f"#{tc} {'Good'}")
    else :
        print(f"#{tc} ", *sorted(li_copy), sep='')