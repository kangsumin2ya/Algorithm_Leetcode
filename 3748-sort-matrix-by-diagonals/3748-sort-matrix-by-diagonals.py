from collections import deque

class Solution:
    def sortMatrix(self, grid):
        # 행렬 크기 정의
        n = len(grid)

        # 대각선 정보 저장할 딕셔너리 초기화
        diags = {}

        # 동일 대각선 상 요소 저장
        for i in range(n):
            for j in range(n):
                k = i - j
                if k not in diags:
                    diags[k] = []
                diags[k].append(grid[i][j])

        # 정렬 (아래쪽은 내림차순, 위쪽은 오름차순)
        for k in diags:
            if k >= 0:
                diags[k].sort(reverse=True)
            else:
                diags[k].sort()

            # pop-left 하기 위해 deque로 변환
            diags[k] = deque(diags[k])  

        # 행렬에 값 다시 채워넣기
        for i in range(n):
            for j in range(n):
                k = i - j
                grid[i][j] = diags[k].popleft()

        return grid
