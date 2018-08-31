class linkedListElement():
    def __init__(self):
        self.value = None
        self.next = None

class linkedList():
    def __init__(self):
        self.start = None
        self.end = None

    def push(self, x):
        order = linkedListElement()
        order.value = x
        if self.start:
            self.end.next = order
            self.end = order
        else:
            self.start = order
            self.end = order

    def remove(self, x):
        tmp = self.start

        if tmp.value == x:
            self.start = self.start.next
        else:
            while tmp.next:
                if tmp.next.value == x:
                    if tmp.next.next:
                        tmp.next = tmp.next.next
                    else:
                        tmp.next = None
                        self.end = tmp
                    break
                else:
                    tmp = tmp.next

    def get(self, x):
        cur = self.start
        idx = 1
        while cur is not None:
            if cur.value == x:
                return idx
            else:
                cur = cur.next
                idx += 1
        else:
            return -1


