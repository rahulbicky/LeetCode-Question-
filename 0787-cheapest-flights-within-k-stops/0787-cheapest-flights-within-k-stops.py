class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(k + 1):

            temp = dist.copy()

            for u, v, price in flights:

                if dist[u] != float('inf'):
                    temp[v] = min(temp[v], dist[u] + price)

            dist = temp

        if dist[dst] == float('inf'):
            return -1

        return dist[dst]