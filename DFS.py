
def init(self):
    self.graph = {'A' : set(['B', 'C']), 'B': set(['A', 'D', 'E']),'C':set(['A', 'F']),'D':set(['B']), 'E': (['B', 'F']), 'F': (['C', 'E'])}

def addEdge (self, u, v):
    self.graph[u].append(v)
    
def DFSUtil(self, v, visited):
    visited[v] = True
    print(v)
    
    for i in self.graph[v]:
        if visited[i] == False:
            self.DFSUtil(i, visited)
            
def DFS(self, v):
    visited = False * len(self.graph)
    self.DFSUtil(v,visited)
    
def DFSUtil(self, v, visited):
    visited[v] = True
    print(v)
    
    for i in self.graph[v]:
        if visited[i] == False:
            self.DFSUtil(i, visited)
def DFS(self, v):
    visited = False * len(self.graph)
    self.DFSUtil(v,visited)
    
