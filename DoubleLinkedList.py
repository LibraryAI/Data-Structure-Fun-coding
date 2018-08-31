class doubleLinkedListElement():
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

class doubleLinkedList():
    def __init__(self):
        self.start = None
        self.end = None

    def insert(self, x, idx = "end"):
        order = doubleLinkedListElement()
        order.value = x
        if self.start:
            if idx == "end":
                self.end.next = order
                order.prev = self.end
                self.end = order
            else:
                cur = self.start
                i = 1
                while i < idx-1:
                    cur = cur.next
                    i += 1
                order.prev = cur
                order.next = cur.next
                cur.next.prev = order
                cur.next = order
        else:
            self.start = order
            self.end = order

    def remove(self, x):
        tmp = self.start

        if tmp.value == x:
            self.start.value = None
            self.start = self.start.next
        else:
            while tmp.next:
                if tmp.next.value == x:
                    if tmp.next.next:
                        tmp.next.value = None
                        tmp.next = tmp.next.next
                    else:
                        tmp.next = None
                        self.end = tmp
                    break
                else:
                    tmp = tmp.next

    def getIdx(self, x):
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

    def getValue(self, x):
        cur = self.start
        idx = 1
        while cur is not None:
            if idx == x:
                return cur.value
            else:
                idx += 1
                cur = cur.next
#insert(x, n), remove(x), getIdx(x), getValue(x)