class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(self.vertices)}
        self.visited = [False]*self.vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, v):
        self.visited[v] = True
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if self.visited[neighbor] == False:
                self.DFS(neighbor)

    def BFS(self, start):
        self.visited = [False] * self.vertices
        queue = []
        self.BFSRecursion(start, queue)

    def BFSRecursion(self, start, queue):
        self.visited[start] = True
        queue.append(start)

        if len(queue) > 0:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for i in self.graph[vertex]:
                if not self.visited[i]:
                    self.BFSRecursion(i,queue)

# Usage
g = Graph(5)
g.add_edge(0, 1)
# g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("DFS:")
g.DFS(2)

print("\nBFS:")
g.BFS(2)