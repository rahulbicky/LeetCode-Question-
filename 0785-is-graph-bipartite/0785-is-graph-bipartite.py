class Solution:
    # Helper DFS to try coloring one component
    def dfs(self, current_node, visited, graph, color):
        visited[current_node] = color          # paint current node
        for adjNode in graph[current_node]:    # go through all neighbors
            if visited[adjNode] != -1:         # neighbor already colored
                if visited[adjNode] == color:  # same color → clash!
                    return False
            else:
                # color neighbor with opposite color (1 - color)
                ans = self.dfs(adjNode, visited, graph, 1 - color)
                if ans == False:               # clash found deeper
                    return False
        return True                            # this branch is fine

    def isBipartite(self, graph: List[List[int]]) -> bool:
        total_nodes = len(graph)
        visited = [-1] * total_nodes           # -1 means "no color yet"
        for index in range(0, total_nodes):
            if visited[index] == -1:           # unvisited component
                ans = self.dfs(index, visited, graph, 0)  # start with color 0
                if ans == False:               # clash in this component
                    return False
        return True                            # all components are okay
        