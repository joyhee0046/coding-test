#파일 읽기
# import sys
# sys.stdin = open("input.txt", "r")

#테스트 케이스 돌리면서 입력받기
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    #비교할 정답 비트
    ansbit = [1 for _ in range(N)]
    #변환된 이진수표현을 저장할 리스트 생성
    bit = [0]
    #이진수 변환
    while M != 0:
        mod = M % 2
        M = M // 2
        bit.insert(-1, mod)
    #변환된 표현이 정답비트와 일치하는지 확인
    if bit[:N] == ansbit:
        ans ="ON"
    else :
        ans ="OFF"
    print(f"#{tc} {ans}")