# import sys
# sys.stdin = open("input.txt", "r")

#테스트케이스 진행하며 입력받기.
for tc in range(1,11):
    N = int(input())
    li = list(input())

    #후위표기법으로 바꾸기
    postfix = []
    keep=[]
    for i in range(N):
        keep.append(li[i])
        if i % 2 == 0:
            while keep != []:
                postfix.append(keep.pop())
    #연산하기
    ans =0
    calculator = []
    for i in range(N):
        if postfix[i] != "+":
            calculator.append(int(postfix[i]))
        else :
            ans = ans + sum(calculator)
            calculator = []
    print(f"#{tc} {ans}")
