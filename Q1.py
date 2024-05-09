class graph_traversal:
    def __init__(self, V):
        self.V = V 
        self.adj = [[] for i in range(V+1)]

    def addEdge(self, v, w):
        self.adj[v].append(w) # Add w to v’s list.

    # prints all not yet visited vertices reachable from s 
    def DFS(self,s):            # prints all vertices in DFS manner from a given source.
                                # Initially mark all vertices as not visited 
        visited = [False for i in range(self.V+1)] 
 
        # Create a stack for DFS 
        stack = []
 
        # Push the current source node. 
        stack.append(s) 
 
        while (len(stack)): 
            # Pop a vertex from stack and print it 
            s = stack[-1] 
            stack.pop()
 
            # Stack may contain same vertex twice. So 
            # we need to print the popped item only 
            # if it is not visited. 
            if (not visited[s]): 
                print(s,end=' ')
                visited[s] = True
 
            # Get all adjacent vertices of the popped vertex s 
            # If a adjacent has not been visited, then push it 
            # to the stack. 
            for node in self.adj[s]: 
                if (not visited[node]): 
                    stack.append(node) 
 
 
# Driver program to test methods of graph_traversal class 
 
g = graph_traversal(25); # Total 25 vertices in graph 
g.addEdge(1, 2); 
g.addEdge(1, 6); 
g.addEdge(2, 3); 
g.addEdge(3, 8); 
g.addEdge(8, 3); 
g.addEdge(8, 9); 
g.addEdge(8, 13); 
g.addEdge(8, 7); 
g.addEdge(7, 8); 
g.addEdge(9, 10); 
g.addEdge(10, 5); 
g.addEdge(10, 15); 
g.addEdge(5, 4);    
g.addEdge(15, 20); 
g.addEdge(20, 19); 
g.addEdge(19, 14);   
g.addEdge(13, 18); 
g.addEdge(18, 23); 
g.addEdge(23, 24); 
g.addEdge(24, 25); 
g.addEdge(12, 7); 
g.addEdge(7, 12); 
g.addEdge(6, 11); 
g.addEdge(11, 12); 
g.addEdge(12, 17); 
g.addEdge(17, 16); 
g.addEdge(17, 22); 
g.addEdge(16, 21);      
 
print("Following is Depth First Traversal") 
g.DFS(1)