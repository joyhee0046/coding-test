T = int(input())


for i in range(1, T + 1):
    ans = False
    da = input()
    da_year = da[0:4]
    da_month = da[4:6]
    da_day = da[6:8]
    if int(da_month) in (1,3,5,7,8,10,12) :
        if int(da_day) < 32 :
            ans = True
    elif int(da_month) in (4,6,9,11) :
        if int(da_day) < 31 :
            ans = True
    elif int(da_month) == 2 :
        if int(da_day) <29 :
            ans = True
    
    if ans :
        print("#{} {}{}{}{}{}".format(i,da_year,"/",da_month,"/",da_day))
    else:
        print("#{} {}".format(i,-1))