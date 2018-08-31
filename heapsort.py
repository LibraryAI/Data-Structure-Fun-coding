class priorityQueue:
    '''
    PriorityQueue를 힙으로 구현
    '''
    def __init__(self) :
        self.data = [0]

    def push(self, value) :
        '''
        PriorityQueue에 value를 삽입
        '''
        self.data.append(value)
        idx = len(self.data)-1
        
        while idx != 1 and self.data[idx] < self.data[idx//2] :
            temp = self.data[idx]
            self.data[idx] = self.data[idx//2]
            self.data[idx//2] = temp
            
            idx = idx // 2

    def top(self) :
        '''
        Return first value
        '''
        return self.data[1]

    def pop(self) :
        '''
        Delete first value 그리고 rearrange
        '''
        if len(self.data) <= 1 :
            return
            
        self.data[1] = self.data[-1]
        self.data.pop()
        
        idx = 1
        
        while True :
            min_idx = -1 
            
            if idx*2 > len(self.data)-1 and idx*2+1 > len(self.data)-1 :
                break
                
            elif idx*2+1 > len(self.data)-1 :
                min_idx = idx*2
                
            else :
                if self.data[idx*2] > self.data[idx*2+1] :
                    min_idx = idx*2+1
                else :
                    min_idx = idx*2
                
            if self.data[idx] > self.data[min_idx] :
                temp = self.data[idx]
                self.data[idx] = self.data[min_idx]
                self.data[min_idx] = temp
                
                idx = min_idx
            else :
                break

def heapSort(items) :
    '''
    PriorityQueue를 이용한 heapsort 구현
    '''
    result = []
    a = priorityQueue()
    for i in items:
        a.push(i)
            
    while len(a.data) > 1:
        result.append(a.top())
        a.pop()

    return result