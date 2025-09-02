from collections import deque

class RecentCounter:

    def __init__(self):
        # 요청 시간 저장할 큐 정의
        self.pings = deque()
        

    def ping(self, t: int) -> int:
        # 요청 시간 저장
        self.pings.append(t)

        # 3000ms외의 요청 제거
        while self.pings and self.pings[0] < t - 3000:
            self.pings.popleft()
        
        # 요청 개수 반환
        return len(self.pings)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)