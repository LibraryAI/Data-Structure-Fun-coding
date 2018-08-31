class Graph :
    def __init__(self, n) :
        '''
        정점이 n개가 있는 그래프 생성
        '''
        self.data = [[0 for i in range(n)] for j in range(n)]

    def addEdge(self, v, w) :
        '''
        간선 (v, w) 추가
        '''
        if len(self.data) >= v and len(self.data[0]) >= w:
            self.data[v-1][w-1] = self.data[w-1][v-1] = 1

    def isEdge(self, v, w) :
        '''
        정점 v와 w가 인접해있으면 True, 아니면 False를 반환
        '''
        if self.data[v-1][w-1] == 1:
            return True
        else:
            return False

    def getAdj(self, v) :
        '''
        정점 v와 인접한 모든 정점을 리스트로 반환
        '''
        result = []
        for i in range(len(self.data[v-1])):
            if self.data[v-1][i] == 1:
                result.append(i+1)
        return result

class Graph :
    def __init__(self, n) :
        '''
        정점이 n개가 있는 그래프 생성
        '''
        self.data = [[] for i in range(n+1)]

    def addEdge(self, v, w) :
        '''
        간선 (v, w) 추가
        '''
        if len(self.data) > v and len(self.data) > w:
            self.data[v].append(w)
            self.data[w].append(v)
        

    def isEdge(self, v, w) :
        '''
        정점 v와 w가 인접해있으면 True, 아니면 False를 반환
        '''
        for i in self.data[v]:
            if i == w:
                return True
            else:
                return False

    def getAdj(self, v) :
        '''
        정점 v와 인접한 모든 정점을 리스트로 반환
        '''
        return self.data[v]