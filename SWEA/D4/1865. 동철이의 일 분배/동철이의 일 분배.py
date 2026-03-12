def solve():
    visited = [False] * n  # 각 열의 방문 여부
    max_prob = 0

    def dfs(row, current_prob):
        nonlocal max_prob

        # 1. 기저 조건 설정
        if row == n:
            if current_prob >= max_prob:
                # print(visited)
                max_prob = current_prob
                # print(max_prob)
            return

        # 2. 행 안에서 열별로 순회
        for col in range(n):
            if not visited[col]:
                next_prob = current_prob * my_data[row][col]
                if next_prob <= max_prob:
                    continue  # 가지치기: 곱했는데 현재 최대보다 더 작거나 같다면 pass
                else:
                    visited[col] = True  # visit 처리 및 몇번 열을 썼는지 기록
                    dfs(row+1, next_prob)

                    # unvisit 처리
                    visited[col] = False

    dfs(0, 1)
    return max_prob


tc = int(input())

for case in range(1, tc + 1):
    n = int(input())
    #  백분율로 표시된 데이터 실제 확률 (0.xx)로 변환해 저장
    my_data = [list(map(lambda x: int(x)/100, input().split())) for _ in range(n)]

    result = solve()
    print(f'#{case} {result*100:.6f}')