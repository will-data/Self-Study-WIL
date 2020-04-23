class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self, head):
        if head == None or head.next == None:
            return (head)
        else:
            checkDuplicate = [head.data]
            current = head
            while current.next:
                if current.next.data in checkDuplicate:
                    current.next = current.next.next
                else:
                    checkDuplicate.append(current.next.data)
                    current = current.next
            return (head)

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head,data)
head = mylist.removeDuplicates(head)
mylist.display(head);