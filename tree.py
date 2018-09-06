class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r

    def addNode(self, i, l, r) :
        # for the node i, assign left child l, right child r
        flag = True
        if self.index == None or self.index == i :
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None

            return True

        else :

            if flag and self.left != None :
                self.left = self.left.addNode(i, l, r)

            if flag and self.right != None :
                self.right = self.right.addNode(i, l, r)


def getHeight(myTree) :
    '''
    myTree의 높이를 반환
    '''
    result = 0

    if myTree == None or myTree.index == -1:
        return result
    else:
        result = result + 1
        result = result + max(getHeight(myTree.left), getHeight(myTree.right))
        return result
