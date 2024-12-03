T = int(input())  # 테스트 케이스 수

# 상, 하, 좌, 우 방향에 대한 이동 정보
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 각 테스트 케이스 처리
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())  # N: 격자 크기, M: 격리 시간, K: 군집 수
    virus_info = [list(map(int, input().split())) for _ in range(K)]  # 초기 군집 정보 입력
    
    for _ in range(M):  # M시간 동안 진행
        new_positions = {}  # 군집이 이동한 후 새로운 위치에 따른 군집 정보 저장
        
        # 군집 이동 처리
        for i in range(len(virus_info)):
            # 미생물 군집이 이동할 방향에 맞게 위치 변경
            virus_info[i][0] += move[virus_info[i][3] - 1][0]
            virus_info[i][1] += move[virus_info[i][3] - 1][1]
            
            # 경계에 도달한 경우
            if not 1 <= virus_info[i][0] < N - 1:  # 세로 방향 경계 체크
                if virus_info[i][3] == 1:
                    virus_info[i][3] = 2  # 상 -> 하
                else:
                    virus_info[i][3] = 1  # 하 -> 상
                virus_info[i][2] //= 2  # 미생물 수 반으로 줄어듬
            
            if not 1 <= virus_info[i][1] < N - 1:  # 가로 방향 경계 체크
                if virus_info[i][3] == 3:
                    virus_info[i][3] = 4  # 좌 -> 우
                else:
                    virus_info[i][3] = 3  # 우 -> 좌
                virus_info[i][2] //= 2  # 미생물 수 반으로 줄어듬
            
            # 새로운 위치에 군집 저장
            if (virus_info[i][0], virus_info[i][1]) not in new_positions:
                new_positions[(virus_info[i][0], virus_info[i][1])] = []
            new_positions[(virus_info[i][0], virus_info[i][1])].append(virus_info[i])
        
        # 군집 합병 처리
        virus_info = []  # 새로운 군집 정보 초기화
        for key, group in new_positions.items():  # 새로운 위치에서 군집 합병
            if len(group) > 1:  # 여러 군집이 모일 경우
                total_count = sum(x[2] for x in group)  # 미생물 수 합산
                max_count, max_dir = max(group, key=lambda x: x[2])[2:4]  # 미생물 수가 많은 군집의 방향
                virus_info.append([key[0], key[1], total_count, max_dir])
            else:  # 한 군집만 있는 경우 그대로 추가
                virus_info.append(group[0])
    
    # 남은 미생물 수 총합 계산
    result = sum(count for _, _, count, _ in virus_info)
    
    print(f'#{test_case} {result}')
