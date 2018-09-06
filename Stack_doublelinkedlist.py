class doubleLinkedListElement():
    '''
    prev: 양방향 서치가 가능한 previous 인스턴스 변수 추가
    '''
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

class doubleLinkedList():
    '''
    count: 전체 element의 수 저장, 1부터 시작

    '''
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    def insert(self, x, idx = "end"):

        # 주어진 인덱스의 위치에 데이터 삽입
        # 삽입하는 데이터에 해당하는 element 와 앞뒤 element의 next, prev 인스턴스 변수 설정

        order = doubleLinkedListElement()
        order.value = x
        if self.start != None:
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

        self.count += 1

    def remove(self, x):

        # start element 부터 시작해 x 값 을 지닌 첫 element 제거 후 다음 element와 연결, 다음 element는 이전 element와 연결

        assert self.start != None
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
                        tmp.next.prev = tmp
                        self.count -= 1
                    else:
                        tmp.next = None
                        self.end = tmp
                        self.count -= 1
                    break
                else:
                    tmp = tmp.next

    def getIdx(self, x):

        # 데이터 x에 해당하는 인덱스 반환

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

    def getValue(self, idx):

        # 데이터를 반환하고자 하는 인덱스와 전체 더블링크드리스트의 element 수를 비교해 탐색
        # 단순 링크드리스트 보다 서치 타임이 1/2 인 장점

        if (self.count // 2) >= idx:
            cur = self.start
            index = 1
            if index == idx:
                return cur.value
            else:
                index += 1
                cur = cur.next
        else:
            cur = self.end
            index = self.count
            if index == idx:
                return cur.value
            else:
                index -= 1
                cur = cur.prev

class Stack:
    '''
    doubleLinkedList 로 Stack 구현
    '''
    def __init__(self):
        self.myStack = doubleLinkedList()

    def push(self, n):
        self.myStack.insert(n)
    
    def pop(self):
        cur = self.myStack.end.prev
        self.myStack.end.value = None
        cur.next = None
        self.myStack.end = cur

    def size(self):
        idx = 1
        cur = self.myStack.start
        while cur.next is not None:
            idx += 1
            cur = cur.next
        return idx

    def empty(self):
        if self.myStack.start is None:
            return True
        else:
            return False

    def top(self):
        return self.myStack.end.value
