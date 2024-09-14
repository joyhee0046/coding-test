# import sys
# sys.stdin = open('input.txt','r')


test_case = int(input())  #몇번 테스트 할거야?

def search_prize(cards, change_num):   # 함수호출하면 시작되는 정의부분
    if change_num == 0:   #변경횟수가 0번 남을때까지 반복
        global max_prize  #밖에서 정의했던 맥스프라이즈 사용하겠다고 선언
        max_prize = max(max_prize, int(''.join(map(str, cards)))) #맥스프라이즈는 max_prize와 카드리스트 중 더 큰 값으로 재정의한다.
        return cards   #종료시점


    for i in range(cards_num-1):  #카드갯수만큼 반복_range가 0부터 시작해서 -1
        for j in range(i + 1, cards_num): #반복문으로 만드는 조합_0부터 시작하는데, 이번에는 시작부분에 +1로 갯수조정
            tmp_cards = cards[:] #원본리스트를 복사하여 임시리스트 생성
            tmp_cards[i], tmp_cards[j] = tmp_cards[j], tmp_cards[i]  #반복문을 통해서 선택한 카드 두 장 자리 바꾸기
            if (change_num, tmp_cards) not in visited:  #만들어진 카드목록와 남은 교환횟수 세트가 이미 확인한 것과 같다면_다시 반복문으로 올라가기
                # print(change_num, tmp_cards, visited, change_num)    #같지 않다면 아래로 진행. // 프린트로 잘 나오고 있는 지 확인
                search_prize(tmp_cards, change_num - 1)   #재귀로 함수 다시 호출. 다음 카드 바꾸기 하려고.
                visited.append((change_num, tmp_cards)) #확인했던 내용 비지티드에 추가하기_다음 탐색에서 확인할 수 있어야 하니까.


for t in range(test_case): # 테케만큼 반복
    cards, change_num = input().split() #입력받기

    cards = [int(num) for num in cards] #입력받은 문자열을 정수 리스트로 만들기_카드리스트
    cards_num = len(cards) #카드갯수확인
    change_num = int(change_num) #입력받은 문자열 정수로 만들기_몇번 교환할건지

    max_prize = 0  #만들어진 가장 큰 수_갱신되도록 가장 작게 설정
    visited = []   #이미 확인한 카드 목록

    search_prize(cards, change_num)   #서치프라이즈 함수 호출, 카드리스트와 교환횟수

    print(f"#{t + 1} {max_prize}")  #형식에 맞춰서 출력