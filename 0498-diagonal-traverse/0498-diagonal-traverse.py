class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 크기 정의
        m, n = len(mat), len(mat[0])

        # 대각선 개수 만큼 리스트 정의
        diagonals = [[] for _ in range(m + n - 1)]

        # 대각선 접근
        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])
        
        # 정답 저장 리스트 정의
        answer = []

        # 대각선 순서에 따라 배열 순서 변경
        for z in range(m + n - 1):
            # 짝수번째면 역순
            if z % 2 == 0:
                answer.extend(diagonals[z][::-1])
            # 홀수번째면 바로 추가
            else:
                answer.extend(diagonals[z])
        
        return answer