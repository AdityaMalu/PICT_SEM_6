class Graph:
    def __init__(self, Nodes, Edges):
        self.adjMatrix = [[0] * 20 for _ in range(20)]
        self.Nodes = Nodes
        self.Edges = Edges
        self.weight = 0

    def add_edge(self, source, destination, weight):
        self.adjMatrix[source][destination] = weight

    def display(self):
        for i in range(self.Nodes):
            for j in range(self.Nodes):
                if self.adjMatrix[i][j] != 0:
                    print(f"{i} - {j} : {self.adjMatrix[i][j]}")

    def create(self):
        for i in range(self.Edges):
            source = int(input("Enter Source: "))
            destination = int(input("Enter Destination: "))
            weight = int(input("Enter Weight: "))
            self.add_edge(source, destination, weight)
            self.add_edge(destination, source, weight)

    def heuristic(self, source, destination):
        return abs(source - destination)

    def prims(self):
        edges_no = 0
        selected = [False] * self.Nodes
        selected[0] = True
        min_val = float('inf')
        x = 0
        y = 0

        while edges_no < self.Nodes - 1:
            min_val = float('inf')
            x = 0
            y = 0

            for i in range(self.Nodes):
                if selected[i]:
                    for j in range(self.Nodes):
                        if not selected[j] and self.adjMatrix[i][j]:
                            total = self.adjMatrix[i][j] + self.heuristic(i, j)
                            if min_val > total:
                                min_val = total
                                x = i
                                y = j

            print(f"{x} - {y} : {self.adjMatrix[x][y]}")
            self.weight += self.adjMatrix[x][y]
            print()

            selected[y] = True
            edges_no += 1

        print(f"Weight of minimum spanning tree: {self.weight}")


def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

# Menu-based program
while True:
    print("\nMenu:")
    print("1. Selection Sort")
    print("2. Prim's Algorithm")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        # Selection Sort
        user_array = list(map(int, input("Enter the elements of the array separated by space: ").split()))
        print("Original Array:", user_array)
        selection_sort(user_array)
        print("Sorted Array:", user_array)

    elif choice == '2':
        # Prim's Algorithm
        vertices = int(input("Enter the number of vertices: "))
        edges = int(input("Enter the number of edges: "))
        graph = Graph(vertices, edges)

        graph.create()

        print("Graph Edges:2")
        graph.display()
        print()

        print("Minimum Spanning Tree Edges (Prim's algorithm):")
        graph.prims()

    elif choice == '3':
        print("Exiting the program.")
        break

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
