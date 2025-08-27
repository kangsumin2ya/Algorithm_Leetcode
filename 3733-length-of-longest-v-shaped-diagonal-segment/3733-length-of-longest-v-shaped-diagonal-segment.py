class Solution:
    def lenOfVDiagonal(self, grid):
        n, m = len(grid), len(grid[0])
        dx = [1, 1, -1, -1]
        dy = [1, -1, -1, 1]

        from functools import lru_cache
        
        # DFS + 메모이제이션 함수
        # x, y 위치, 방향 d, 턴 사용 여부 turn(0/1), next 기대값(2 또는 0)
        @lru_cache(None)
        def dfs(x, y, d, turn, next_val):
            # 범위 벗어나거나 패턴 불일치 시 0 반환
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] != next_val:
                return 0

            # 다음 기대값 토글(2 <-> 0)
            next_expect = 0 if next_val == 2 else 2

            res = 0
            # 직진
            res = max(res, 1 + dfs(x + dx[d], y + dy[d], d, turn, next_expect))

            # 턴 가능하면 한 번 턴
            if turn == 0:
                nd = (d + 1) % 4  # 시계 방향으로 한 번 턴
                res = max(res, 1 + dfs(x + dx[nd], y + dy[nd], nd, 1, next_expect))
            return res

        max_len = 0
        # 시작점은 grid[i][j] == 1이고, next_val은 2부터 시작
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        max_len = max(max_len, 1 + dfs(i + dx[d], j + dy[d], d, 0, 2))
        return max_len
