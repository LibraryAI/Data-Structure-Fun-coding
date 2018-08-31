class Stack:
    '''
    List를 이용한 Stack
    '''
    def __init__(self) :
        # Stack 생성
        self.myStack = []

    def push(self, n) :
        # Stack에  data 삽입
        self.myStack.append(n)

    def pop(self) :
        # Stack의 맨 위에 있는 data 제거
        self.myStack.pop()

    def size(self) :
        # Stack에 있는 data 수 반환
        return len(self.myStack)

    def empty(self) :
        # If empty return 1 else return 0
        if len(self.myStack) == 0:
            return 1
        else:
            return 0

    def top(self) :
        # return top of the stack, if empty return -1
        if len(self.myStack) == 0:
            return -1
        else:
            return self.myStack[-1]
