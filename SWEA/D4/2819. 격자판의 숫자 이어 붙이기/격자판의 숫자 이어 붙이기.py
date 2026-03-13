def solve():

    def dfs(row, col, num_cnt, current_str):
        """
        현재 좌표에서 갈 수 있는 다른 좌표들로 깊이 들어가면서
        num_cnt 가 7이 되면 이를 저장하고 리턴
        """
        # 0. 기저조건 설정
        if num_cnt == 7:
            current_int = int(current_str)
            data.add(current_int)
            return
        # 1. 현재 좌표에서 갈 수 있는 다른 좌표들을 확인
        for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ny = row + dy
            nx = col + dx
            # 2. 유효한 범위에 있는 수면 현 상태에 더하고 재귀호출
            if -1 < ny < 4 and -1 < nx < 4:
                dfs(ny, nx, num_cnt+1, current_str+space[ny][nx])

    data = set()
    for r in range(4):
        for c in range(4):
            # 모든 가능한 시작점에 대해 dfs 시작
            dfs(r, c, 1, space[r][c])

    return len(data)


tc = int(input())

for case in range(1, tc + 1):
    space = [list(input().split()) for _ in range(4)]

    result = solve()
    print(f'#{case} {result}')