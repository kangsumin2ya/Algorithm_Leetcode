import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # s가 t를 반복해 만들어지는지 확인하는 함수
        def divides(s, t):
            # 나누어 떨어지지 않으면 t 반복해서 만들기 불가능
            if len(s) % len(t) != 0:
                return False
            # t를 s길이에서 t길이를 나눈 몫만큼 반복한 문자열이 s면 True, 아님 False
            return s == t * (len(s) // len(t))

        # 문자열 길이의 최대공약수 구하기
        gcd_len = math.gcd(len(str1), len(str2))

        # str1 중 길이가 최대공약수인 부분을 후보 설정
        candidate = str1[:gcd_len]

        # 반복해서 만들 수 있는지 확인
        if divides(str1, candidate) and divides(str2, candidate):
            # 되면 최대공약수 문자열 맞음
            return candidate
        else:
            # 아니면 빈 문자열
            return ""
