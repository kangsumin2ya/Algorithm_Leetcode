class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 길이 비교해 더 짧은 배열을 nums1으로 두기
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # 길이 저장 변수 정의
        m, n = len(nums1), len(nums2)

        # 왼쪽, 오른쪽 정의
        left, right = 0, m

        # 이진탐색 시작
        while left <= right:
            # nums1은 i, nums2는 j에서 자르기
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # 최솟값, 최댓값 지정
            max_left_nums1 = float('-inf') if i == 0 else nums1[i-1]
            min_right_nums1 = float('inf') if i == m else nums1[i]
            max_left_nums2 = float('-inf') if j == 0 else nums2[j-1]
            min_right_nums2 = float('inf') if j == n else nums2[j]

            # 잘 분할되었는지 확인
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                # 홀수라면 중앙값 반환
                if (m + n) % 2 == 1:
                    return max(max_left_nums1, max_left_nums2)
                # 짝수라면 평균
                else:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                
            
            # 잘 분할 안되었다면 이동
            elif max_left_nums1 > min_right_nums2:
                right = i - 1
            else:
                left = i + 1


        
        
        