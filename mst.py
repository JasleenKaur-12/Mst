class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def kruskal(n, edges):
    # Sort edges based on their weight
    edges.sort(key=lambda edge: edge[2])
    
    # Dynamically create union-find to handle the largest vertex number in the edges
    max_vertex = max(max(u, v) for u, v, _ in edges)
    uf = UnionFind(max_vertex + 1)  # Ensure enough space for all vertices
    
    mst = []
    mst_weight = 0
    
    for u, v, weight in edges:
        if uf.union(u, v):  # If u and v are not in the same set, add edge to MST
            mst.append((u, v, weight))
            mst_weight += weight
            
            # If we already have n-1 edges, MST is complete
            if len(mst) == n - 1:
                break
    
    return mst, mst_weight

# User input:
n = int(input("Enter the number of vertices: "))  # Number of vertices
e = int(input("Enter the number of edges: "))  # Number of edges

edges = []

for _ in range(e):
    u, v, weight = map(int, input("Enter an edge (u v weight): ").split())
    edges.append((u, v, weight))

# Find the MST
mst, mst_weight = kruskal(n, edges)

# Output the MST
print("\nEdges in the Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")

print(f"\nTotal weight of MST: {mst_weight}")
