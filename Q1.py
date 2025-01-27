# Add vertices to their respective adjacency lists
# Since it's an undirected graph, each edge connects two vertices bidirectionally,
# so, add to both adjacency lists
# For example, edge: (1, 2) means that 1 can go to 2 and 2 can go to 1, so add to both adjacency lists
def addEdge(adj, x, y):
    adj[x].append(y) # Add x to y’s list.
    adj[y].append(x) # Add y to x's list       
    
def DFS(V, adj, s):
    # Initializes all vertices as not visited 
    visited = [False for i in range(V+1)] 

    # Create a stack for DFS 
    # Stack is last in first out(LIFO), 
    # and since the adjacency list is filled in ascending order of chamber number,
    # chambers with higher numbers will be popped out first.
    stack = []        

    # Create a list to keep track of visited node
    visitedList = []
    
    # Record the number of chambers visited
    count = 0

    # Push the current source node to the stack
    stack.append(s) 
    
    while (count<V): 
        # Pop a vertex from stack
        s = stack.pop()

        # Stack may contain same vertex twice. Only appends unvisited vertex to the visitedList
        if (not visited[s]): 
            visitedList.append(s)
            print('Visiting chamber ',s)
            # Update the chamber as visited
            visited[s] = True
            count += 1

        # Get all adjacent vertices of the popped vertex s 
        allUnvisited = True
        for node in adj[s]: 
            # If an adjacent vertex has not been visited, then push it to the stack. 
            if (not visited[node]): 
                stack.append(node)
                allUnvisited = False 
        # If all of the adjacent vertices have been visited, backtrack to the unvisited vertex
        if (count !=V and allUnvisited):
            print('Backtracking...')
        
    # Print the sequence of chambers visited
    print("Algo Jones successfully visited all chambers.\nSequence of chambers visited:\n",visitedList)   
                
        
V = 25  # Total 25 vertices in graph
adj = [[] for i in range(V+1)]
# Define all the edges in the graph
edges = [(1,2),(1,6),(2,3),(3,8),(4,5),(5,10),(6,11),(7,8),(7,12),(8,9),(8,13),(9,10),(10,15),(11,12)
         ,(12,17),(13,18),(14,19),(15,20),(16,17),(16,21),(17,22),(18,23),(19,20),(23,24),(24,25)]

# Add edges to the adjacency lists
for edge in edges:
    addEdge(adj, edge[0],edge[1])

 
print("Algo Jones began his search in the Pyramid of Khufu...") 
DFS(V, adj, 1) # Entrance is chamber 1