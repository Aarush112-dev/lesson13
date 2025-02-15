class Graph:
    def __init__(self,num_nodes):
        self.graph = {}
        self.sides = num_nodes
        for i in range(1,self.sides+1):
            self.graph[i] = []
    
    def add_edge(self,x,y):
        self.graph[x].append(y)

    def iscyclic(self,n,visited,rstack):
        visited[n] = True
        rstack[n] = True
        for node in self.graph[n]:
            print(node)
            if visited[node] == False:
                if self.iscyclic(node,visited,rstack):
                    return True
            elif rstack[node] == True:
                return True
        rstack[n] = False
        return False
    
    def checkcyclic(self):
        visited = [False] * self.sides+1
        rstack = [False] * self.sides+1
        for i in range(1,self.sides+1):
            if visited[i] == False:
                if self.iscyclic(i,visited,rstack):
                    return True
        return False

        

graph1 = Graph(7)
graph1.add_edge(1,2)
graph1.add_edge(2,3)
graph1.add_edge(3,5)
graph1.add_edge(5,6)
graph1.add_edge(6,7)
graph1.add_edge(7,3)
print(graph1.graph)
if graph1.checkcyclic() == True:
    print("There is a cycle")
else:
    print("There isn't a cycle")

        
