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


class Ended(Exception):
    pass


def relax(prioqueue, visited, distances, src_tile, dst_tile, dst):
    if dst_tile.distance > src_tile.distance + dst_tile.val:
        if not visited[dst_tile[0]][dst_tile[1]]:
            heappush(prioqueue, PrioritizedNode(dst_tile[0], dst_tile[1], src_tile.distance + dst_tile.val))
        distances[dst_tile[0]][dst_tile[1]] = src_tile.distance + dst_tile.val
        if dst_tile == dst:
            raise Ended


def dijkstra(graph: "list[list[int]]", src, dst):
    prioqueue = []
    distances = []
    previouses = []
    visited = []
    for x, line in enumerate(graph):
        distances.append([])
        previouses.append([])
        visited.append([])
        for y, tile_val in enumerate(line):
            if (x, y) != src:
                heappush(prioqueue, PrioritizedNode(x, y, inf))
                distances[x].append(inf)
            else:
                heappush(prioqueue, PrioritizedNode(x, y, 0))
                distances[x].append(0)
            previouses[x].append(None)
            visited[x].append(False)

    try:
        while len(prioqueue) > 0:
            curr_tile = heappop(prioqueue)
            while visited[curr_tile.x][curr_tile.y]:
                curr_tile = heappop(prioqueue)
            if curr_tile.x > 0:
                relax(prioqueue, visited, distances, (curr_tile.x, curr_tile.y), (curr_tile.x - 1, curr_tile.y))
            if curr_tile.y > 0:
                relax(prioqueue, visited, distances, (curr_tile.x, curr_tile.y), (curr_tile.x, curr_tile.y - 1))
            if curr_tile.x < len(graph) - 1:
                relax(prioqueue, visited, distances, (curr_tile.x, curr_tile.y), (curr_tile.x + 1, curr_tile.y))
            if curr_tile.y < len(graph[0]) - 1:
                relax(prioqueue, visited, distances, (curr_tile.x, curr_tile.y), (curr_tile.x, curr_tile.y + 1))
            visited[curr_tile.x][curr_tile.y] = True
    except Ended:
        pass
