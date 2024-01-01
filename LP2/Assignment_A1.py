from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.visited = defaultdict(bool)
        self.adj = defaultdict(list)

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def BFS(self, v, q):
        if not q:
            return

        v = q.popleft()

        if not self.visited[v]:
            self.visited[v] = True
            print(v, end=' ')

            for i in self.adj[v]:
                if not self.visited[i]:
                    q.append(i)

        self.BFS(v, q)

    def DFS(self, v):
        self.visited[v] = True
        print(v, end=' ')

        for i in self.adj[v]:
            if not self.visited[i]:
                self.DFS(i)

g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 3)
g.addEdge(1, 2)
g.addEdge(2, 4)

print("Enter 1 for DFS and 2 for BFS: ", end='')
choice = int(input())
if choice == 1:
    print("Following is Depth First Traversal: ")
    g.DFS(2)
elif choice == 2:
    print("Following is Breadth First Traversal: ")
    q = deque()
    q.append(2)
    g.BFS(2, q)
else:
    print("Invalid choice")