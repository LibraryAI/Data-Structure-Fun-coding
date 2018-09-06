
#Graph class의 method의 역할은 모두 동일

class Graph :
    '''
    매트릭스 형식의 그래프
    - 연결 여부에 대한 반환의 속도가 빠름
    - 인정 정점 반환이 len(mat) size 만큼의 iteration을 돌아서 느림
    '''
    def __init__(self, n) :

        # 정점이 n개가 있는 그래프 생성
        self.data = [[0 for i in range(n)] for j in range(n)]

    def addEdge(self, v, w) :
        
        # 간선 (v, w) 추가
        if len(self.data) >= v and len(self.data[0]) >= w:
            self.data[v-1][w-1] = self.data[w-1][v-1] = 1

    def isEdge(self, v, w) :
        
        #정점 v와 w가 인접해있으면 True, 아니면 False를 반환
        
        if self.data[v-1][w-1] == 1:
            return True
        else:
            return False

    def getAdj(self, v) :
        
        # 정점 v와 인접한 모든 정점을 리스트로 반환
        
        result = []
        for i in range(len(self.data[v-1])):
            if self.data[v-1][i] == 1:
                result.append(i+1)
        return result

class Graph :
    '''
    리스트 형식의 그래프
    - 연결 여부 확인이 느림
    - 연결 정점 반환이 빠름
    '''
    def __init__(self, n) :
        
        # 정점이 n개가 있는 그래프 생성
        
        self.data = [[] for i in range(n+1)]

    def addEdge(self, v, w) :
        
        # 간선 (v, w) 추가
        
        if len(self.data) > v and len(self.data) > w:
            self.data[v].append(w)
            self.data[w].append(v)
        

    def isEdge(self, v, w) :
        
        # 정점 v와 w가 인접해있으면 True, 아니면 False를 반환
        
        for i in self.data[v]:
            if i == w:
                return True
            else:
                return False

    def getAdj(self, v) :
        
        # 정점 v와 인접한 모든 정점을 리스트로 반환
        
        return self.data[v]

def DFS(n, m, myInput) :
    '''
    정점이 n개, 간선이 m개인 그래프의 정보가 myInput으로 주어질 때, 1부터 시작하여 그래프를 깊이우선탐색한 결과를 리스트로 반환
    '''
    #linked list 로 만들어야 O(g(V))속도가 나와서 더 빠름
    a = graph(n)
    for i in myInput:
        a.addEdge(i[0], i[1])
    result = [1]
    result = result + inDFS(a.data, [1])
    
    return result
