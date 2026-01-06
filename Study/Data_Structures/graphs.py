class Graph:
    def __init__(self, directed=False, weighted=False):
        self.directed=directed
        self.weighted=weighted
        self.adj_list = {}


    def __len__(self):
        return len(self.adj_list)


    def __str__(self):
        result = ""
        for node in self.adj_list:
            result += f"{node} -> {self.adj_list[node]}\n"
        return result


    def insert_node(self, node):
        if node not in self.adj_list: #if node not already in graph add the node
            self.adj_list[node] = [] #no edges


    def insert_edge(self, node1,node2,weight=1): #Adds an edge between two nodes
        if node1 not in self.adj_list: #add nodes to list if theyre not there already
            self.insert_node(node1)
        if node2 not in self.adj_list:
            self.insert_node(node2)

        self.adj_list[node1].append((node2, weight)) #adds the edge to the node

        if not self.directed: # If undirected, add reverse edge also
            self.adj_list[node2].append((node1, weight))


    def delete_node(self, node): #Removes a vertex from the graph.
        if node not in self.adj_list:
            return

        for v in self.adj_list: #All edges pointing to this node are removed from other nodes
            self.adj_list[v] = [
                (n, w) for (n, w) in self.adj_list[v] if n != node
            ]

        del self.adj_list[node] #node itself is deleted from adjacency list


    def delete_edge(self,node1,node2): #Removes the edge from node1 to node2
        if node1 not in self.adj_list or node2 not in self.adj_list: #If nodes not in list then return
            return

        self.adj_list[node1] = [(n, w) for (n, w) in self.adj_list[node1] if n != node2] #goes through all edges connectd to node1 and remove edge also connected to node2

        if not self.directed:
            self.adj_list[node2] = [(n, w) for (n, w) in self.adj_list[node2] if n != node1] # If undirected, remove reverse edge also


g = Graph(directed=False, weighted=False)
g.insert_edge("A", "B")
g.insert_edge("A", "C")
g2 = Graph(directed=True, weighted=True)
g2.insert_edge("A", "B", 5)
g2.insert_edge("B", "C", 2)

print(g)
print(g2)

g.delete_edge("A","C")
print(g)