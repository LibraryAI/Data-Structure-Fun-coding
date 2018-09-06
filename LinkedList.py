class linkedListElement():
    '''
    링크드리스트의 element
    value: 데이터를 저장하는 인스턴스 변수
    next: 다음 element를 저장 (포인터같은 느낌)
    '''
    def __init__(self):
        self.value = None
        self.next = None

class linkedList():
    def __init__(self):
        self.start = None
        self.end = None

    def push(self, x):

        # end에 데이터 삽입

        order = linkedListElement()
        order.value = x
        if self.start:
            self.end.next = order
            self.end = order
        else:
            self.start = order
            self.end = order

    def remove(self, x):

        # start element 부터 시작해 x 값 을 지닌 첫 element 제거 후 다음 element와 연결

        assert self.start != None
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

        # x에 해당하는 element의 인덱스 반환 (여기서는 첫 인덱스가 1)

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


