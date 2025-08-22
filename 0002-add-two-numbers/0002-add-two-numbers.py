# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 리스트 정의
        li_l1 = []
        li_l2 = []

        # 리스트에 넣기
        while True:
            li_l1.append(l1.val)
            if l1.next == None:
                break
            l1 = l1.next

        while True:
            li_l2.append(l2.val)
            if l2.next == None:
                break
            l2 = l2.next

        # 순서 뒤집기
        li_l1 = li_l1[::-1]
        li_l2 = li_l2[::-1]

        # 요소들 문자열로 변환
        for i in range(len(li_l1)):
            li_l1[i] = str(li_l1[i])

        for i in range(len(li_l2)):
            li_l2[i] = str(li_l2[i])
        

        # 리스트 요소 합치기
        li_l1 = ''.join(li_l1)
        li_l2 = ''.join(li_l2)

        # 덧셈 연산 후 형변환하고 리스트에 넣기
        li_answer = list(str(int(li_l1) + int(li_l2)))
        
        # 역순으로 바꾸기
        li_answer = li_answer[::-1]

        # 요소들 정수형으로 변환
        li_answer = [int(x) for x in li_answer]

        # 연결리스트에 넣기
        head = ListNode(li_answer[0])

        current = head
        for i in range(1, len(li_answer)):
            current.next = ListNode(li_answer[i])
            current = current.next

        return head
