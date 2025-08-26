class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # 대각선 길이, 넓이 저장할 리스트 정의
        calculate_list = [[] for _ in range(len(dimensions))]

        # 대각선 길이, 넓이 구하기
        for i in range(len(dimensions)):
            i_diagonal = sqrt(((dimensions[i][0])**2 + (dimensions[i][1])**2))
            i_area = dimensions[i][0] * dimensions[i][1]
            calculate_list[i] = (i_diagonal, i_area)

        # 내림차순 (1순위 : 대각선, 2순위 : 넓이)
        calculate_list.sort(key=lambda x: (-x[0], -x[1]))

        return calculate_list[0][1]