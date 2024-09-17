### 보호필름_DFS
# import sys
# sys.stdin = open('sample_input (3).txt', 'r')

def chk_test():
    # 비교하기 위한 리스트값 미리 준비
    chk_a_list = [0] * K
    chk_b_list = [1] * K
    # 한줄씩 검사하기
    for w_i in range(W):
        is_success = False
        for d_i in range(D - K + 1):
            cur_chk = [film[tmp_i][w_i] for tmp_i in range(d_i, d_i + K)]
            if cur_chk == chk_a_list or cur_chk == chk_b_list:
                is_success = True
                break
        # 통과하지 못했다면 F
        if not is_success:
            return False
    # 통과했다면 T
    return True

def test_film(film, depth=0, cnt_inject=0, chk_list=[]):
    global min_inject
    # 갱신 값을 넘어서 더이상 검증이 무의미한 경우 지나가기
    if cnt_inject >= min_inject:
        return
    # 함수로 넘어가서 약품 넣기
    if chk_test():
        # 최소 약품 투입 횟수로 갱신
        min_inject = min(min_inject, cnt_inject)
        return
    # 최대 깊이를 넘어섰다면 지나가기
    if depth >= D:
        return
    # 원본에 적용되지 않도록 복사하기
    origin_membrane = film[depth][:]
    # 현재 층을 그대로 두고 넘어가는 재귀
    test_film(film, depth + 1, cnt_inject, chk_list + ['0'])
    # 현재 층을 a로 바꾸는 재귀
    film[depth] = inject_a
    test_film(film, depth + 1, cnt_inject + 1, chk_list + ['a'])
    film[depth] = origin_membrane
    # 현재 층을 b로 바꾸는 재귀
    film[depth] = inject_b
    test_film(film, depth + 1, cnt_inject + 1, chk_list + ['b'])
    film[depth] = origin_membrane

# 주어진 입력 받기
T = int(input())
for tc in range(1, 1+T):
    # D: 보호필름 두께, W: 가로크기, K: 합격기준
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    # 한 줄을 모두 특정 값으로 채우기 위해 미리 준비
    inject_a = [0] * W
    inject_b = [1] * W
    # 갱신할 목표 변수 만들기
    min_inject = float('inf')
    # 메인 함수 실행
    test_film(film)
    print(f"#{tc} {min_inject}")