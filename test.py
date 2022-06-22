# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    
    def __init__(self, nestedList: [NestedInteger]):
        def flatten_list(nested_list):
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self.myList.append(nested_integer.getInteger())
                else:
                    flatten_list(nested_integer.getList()) 
        self.myList = []
        self.index = -1 # Pointer to previous returned.
        flatten_list(nestedList)
    
    def next(self) -> int:
        self.index += 1
        return self.myList[self.index]
        
    def hasNext(self) -> bool:
        return self.index + 1 < len(self.myList)
            
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())





class Solution:
    marks = [] # 1 ==  discorvered, 0 undiscovered
    adjList = []
    upper = 0
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n - 1: return -1
        
        self.marks = [] # 1 ==  discorvered, 0 undiscovered
        self.adjList = []
        self.upper = 0
        
        compCount = 0
        
        for point in connections:
            if self.upper < max(point):
                self.upper = max(point)
                
        
        self.upper+=1
        
        for i in range(n):
            self.adjList.append([0]*n)
        
        for j in range(n):
            self.marks.append(0)
            
        
        for p in connections:
            self.adjList[p[0]][p[1]] = 1
            self.adjList[p[1]][p[0]] = 1
            

        for i in range(n):
            if self.marks[i] == 0:
                compCount += 1
                self.dfs(i)
    
        return compCount-1
    
    
######################################################
    def dfs(self, index: int) -> None:
        self.marks[index] = 1
        neigh = self.getNeighbors(index)
        
        for n in neigh:
            if self.marks[n] == 0:
                self.dfs(n)
        
    
    def getNeighbors(self, index: int) -> List[int]:
        ret = []
        for n in range(len(self.adjList)):
            if self.adjList[index][n] == 1:
                ret.append(n)
        return ret
    