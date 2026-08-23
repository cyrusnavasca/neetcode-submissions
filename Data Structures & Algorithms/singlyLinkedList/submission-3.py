class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        # Initialize dummy head
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        count = 0
        while curr:
            if count == index:
                return curr.val
            count += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new = Node(val)
        if not self.head.next: # need to set new as tail also
            self.tail = new
        new.next = self.head.next
        self.head.next = new

    def insertTail(self, val: int) -> None:
        new = Node(val)
        self.tail.next = new
        self.tail = new

    def remove(self, index: int) -> bool:
        prev = self.head
        count = 0
        while prev and count < index:
            prev = prev.next
            count += 1

        if prev and prev.next:
            if prev.next == self.tail:
                self.tail = prev
            prev.next = prev.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res





