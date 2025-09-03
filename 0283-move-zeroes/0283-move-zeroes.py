class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 0 아닌 요소가 들어갈 인덱스 초기화
        idx = 0

        # 요소 확인
        for num in nums:
            # 0이 아니면 앞으로 옮기기
            if num != 0:
                nums[idx] = num
                # 인덱스 증가
                idx += 1
            
        # 남은 공간 0으로 채우기
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
