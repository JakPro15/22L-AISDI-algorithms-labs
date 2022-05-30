from file_reader import read_file
from print_path import show_path, print_tiles
from dijkstra import dijkstra


if __name__ == "__main__":
    print("Graph 1\n")
    tiles = read_file("graf1.txt")
    zeros = []
    for y in tiles:
        for x in tiles:
            if tiles[y][x] == 0:
                zeros.append((x, y))
    path = dijkstra(tiles, zeros[0], zeros[1])
    path_tiles = show_path(tiles, path)
    print_tiles(tiles)
    print('\n')
    print("Path 1\n")
    print_tiles(path_tiles)
    print('\n')
    print("Graph 2\n")
    tiles = read_file("graf2.txt")
    zeros = []
    for y in tiles:
        for x in tiles:
            if tiles[y][x] == 0:
                zeros.append((x, y))
    path = dijkstra(tiles, zeros[0], zeros[1])
    path_tiles = show_path(tiles, path)
    print_tiles(tiles)
    print('\n')
    print("Path 2\n")
    print_tiles(path_tiles)
    print('\n')
    print("Graph 3\n")
    tiles = read_file("graf3.txt")
    path = dijkstra(tiles, zeros[0], zeros[1])
    for y in tiles:
        for x in tiles:
            if tiles[y][x] == 0:
                zeros.append((x, y))
    path = []
    path_tiles = show_path(tiles, path)
    print_tiles(tiles)
    print('\n')
    print("Path 3\n")
    print_tiles(path_tiles)
