class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 만들 수 있는 문자열의 최대 크기 정의
        max_length = max(len(word1), len(word2)) * 2
        # 만들 수 있는 문자열 저장할 리스트 정의
        words = [''] * max_length

        # 각 단어의 현재 인덱스 정의
        i1, i2 = 0, 0

        # 값 넣기
        for i in range(max_length):
            # 짝수번째엔 word1
            if i % 2 == 0:
                # 단어 길이가 최대 길이보다 짧아서 제한
                if i1 < len(word1):
                    words[i] = word1[i1]
                    # 인덱스 증가
                    i1 += 1
            # 홀수번째엔 word2
            else:
                if i2 < len(word2):
                    words[i] = word2[i2]
                    # 인덱스 증가
                    i2 += 1
        
        # 리스트를 한 단어로 합치기
        words = ''.join(words)

        return words
        