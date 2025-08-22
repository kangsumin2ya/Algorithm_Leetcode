class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 임시 리스트, 최대 길이 초기화
        li_temp = []
        max_len = 0

        # 문자열 하나씩 확인
        for char in s:
            # 중복 문자 만났을 때
            if char in li_temp:
                # 중복이 나온 위치 다음부터 남긴다
                idx = li_temp.index(char)
                li_temp = li_temp[idx+1:]

            li_temp.append(char)

            # 길이 더 길면 갱신
            if len(li_temp) > max_len:
                max_len = len(li_temp)

        return max_len
