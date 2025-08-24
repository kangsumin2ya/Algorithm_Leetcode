class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 윈도우 왼쪽 인덱스
        left = 0
        # 윈도우 내 0의 개수
        count_0 = 0
        # 최장 길이
        max_len = 0

        # 윈도우 오른쪽을 옮기면서 탐색
        for right in range(len(nums)):
            # 0이면 개수 증가
            if nums[right] == 0:
                count_0 += 1
            
            # 윈도우 내 0이 2개 이상이면 0이 하나 남을 때까지 left 움직임
            while count_0 > 1:
                # 0인 경우 개수 줄이기
                if nums[left] == 0:
                    count_0 -= 1
                
                # left 움직이기
                left += 1
            
            # 현재 윈도우 길이 중 최댓값 갱신
            max_len = max(max_len, right - left)
    
        return max_len

