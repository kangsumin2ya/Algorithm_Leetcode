class Solution:
    def countBits(self, n: int) -> List[int]:
        # 1의 개수 저장할 리스트 정의
        ans = []

        # 0부터 n까지를 담고 있는 리스트 정의
        n_list = [i for i in range(n+1)]

        # 배열에 접근해 이진수 변환 후 1의 개수 세기
        for n in n_list:
            n_bi = bin(n)
            ans.append(n_bi.count('1'))
        
        return ans