# import sys
# sys.stdin = open('input.txt', 'r')

from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    earthworm_list = [list(map(int, input().split())) for _ in range(N)]

    # visited = []
    #
    # for i in range(len(earthworm_list)-1):
    #     for j in range(i+1, len(earthworm_list)):
    #         ei_y = earthworm_list[i][0]
    #         ei_x = earthworm_list[i][1]
    #
    #         ej_y = earthworm_list[j][0]
    #         ej_x = earthworm_list[j][1]
    #
    #         if (((ei_y, ei_x), (ej_y, ej_x))) not in visited or (((ej_y, ej_x), (ei_y, ei_x))) not in visited:
    #

    num = [number for number in range(N)]
    comb_list = []
    result_list = []
    for comb in combinations(num, int(N / 2)):
        comb_list.append(comb)

    for length in range(len(comb_list) // 2):
        i_num_x = 0
        i_num_y = 0
        for i_num in comb_list[length]:
            i_num_x += earthworm_list[i_num][0]
            i_num_y += earthworm_list[i_num][1]
        j_num_x = 0
        j_num_y = 0
        for j_num in comb_list[-(length + 1)]:
            j_num_x += earthworm_list[j_num][0]
            j_num_y += earthworm_list[j_num][1]

        result_list.append(pow(j_num_x - i_num_x, 2) + pow(j_num_y - i_num_y, 2))

    print(f'#{test_case} {min(result_list)}')