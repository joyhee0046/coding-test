import datetime
T = int(input())

for tc in range(1, T+1) :
    D, H, M = map(int, input().split())
    # da = datetime.date(2011,11,11)
    # ta = datetime.time(11,11,0)
    # db = datetime.date(2011,11,D)
    # tb = datetime.time(H,M,0)
    
    # day = db-da
    # #time = tb-ta
    # print(day,datetime.timedelta()))
    
    
    ans = ((((D-11)*24)+(H-11))*60)+(M-11)
    
    if ans <0 :
        ans = -1
    print(f"#{tc} {ans}")