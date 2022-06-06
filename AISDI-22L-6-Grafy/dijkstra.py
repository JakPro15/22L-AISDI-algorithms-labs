from functools import total_ordering
from math import inf
from heapq import heappush, heappop


@total_ordering
class PrioritizedNode:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __lt__(self, other):
        return self.distance < other.distance


def relax(graph, previouses, prioqueue, visited, distances,
          src_tile, dst_tile):
    new_distance = distances[src_tile[0]][src_tile[1]] + \
        graph[src_tile[0]][src_tile[1]]
    if distances[dst_tile[0]][dst_tile[1]] > new_distance:
        if not visited[dst_tile[0]][dst_tile[1]]:
            heappush(prioqueue,
                     PrioritizedNode(dst_tile[0], dst_tile[1], new_distance))
        distances[dst_tile[0]][dst_tile[1]] = new_distance
        previouses[dst_tile[0]][dst_tile[1]] = src_tile


def dijkstra(graph: "list[list[int]]", src, dst):
    prioqueue = []
    distances = []
    previouses = []
    visited = []
    for x, line in enumerate(graph):
        distances.append([])
        previouses.append([])
        visited.append([])
        for y in range(len(line)):
            if (x, y) != src:
                distances[x].append(inf)
            else:
                heappush(prioqueue, PrioritizedNode(x, y, 0))
                distances[x].append(0)
            previouses[x].append(None)
            visited[x].append(False)

    while len(prioqueue) > 0:
        curr_tile = heappop(prioqueue)
        while visited[curr_tile.x][curr_tile.y]:
            curr_tile = heappop(prioqueue)
        if curr_tile.x > 0:
            relax(graph, previouses, prioqueue, visited, distances,
                  (curr_tile.x, curr_tile.y), (curr_tile.x - 1, curr_tile.y))
        if curr_tile.y > 0:
            relax(graph, previouses, prioqueue, visited, distances,
                  (curr_tile.x, curr_tile.y), (curr_tile.x, curr_tile.y - 1))
        if curr_tile.x < len(graph) - 1:
            relax(graph, previouses, prioqueue, visited, distances,
                  (curr_tile.x, curr_tile.y), (curr_tile.x + 1, curr_tile.y))
        if curr_tile.y < len(graph[0]) - 1:
            relax(graph, previouses, prioqueue, visited, distances,
                  (curr_tile.x, curr_tile.y), (curr_tile.x, curr_tile.y + 1))
        visited[curr_tile.x][curr_tile.y] = True
        if (curr_tile.x, curr_tile.y) == dst:
            break

    curr_tile = dst
    results = [curr_tile]
    while previouses[curr_tile[0]][curr_tile[1]]:
        curr_tile = previouses[curr_tile[0]][curr_tile[1]]
        results.append(curr_tile)

    return results
