from file_reader import read_file
from print_path import show_path, print_tiles
from dijkstra import dijkstra


def find_zeros(tiles):
    zeros = []
    for x, line in enumerate(tiles):
        for y in range(len(line)):
            if tiles[x][y] == 0:
                zeros.append((x, y))
    return zeros


if __name__ == "__main__":
    print("Graph 1\n")
    tiles = read_file("graf1.txt")
    zeros = find_zeros(tiles)
    path = dijkstra(tiles, zeros[0], zeros[1])
    path_tiles = show_path(tiles, path)
    print_tiles(tiles)
    print('\n')
    print("Path 1\n")
    print_tiles(path_tiles)
    print('\n')
    print("Graph 2\n")
    tiles = read_file("graf2.txt")
    zeros = find_zeros(tiles)
    path = dijkstra(tiles, zeros[0], zeros[1])
    path_tiles = show_path(tiles, path)
    print_tiles(tiles)
    print('\n')
    print("Path 2\n")
    print_tiles(path_tiles)
    print('\n')
    print("Graph 3\n")
    tiles = read_file("graf3.txt")
    zeros = find_zeros(tiles)
    path = dijkstra(tiles, zeros[0], zeros[1])
    path_tiles = show_path(tiles, path)
    print_tiles(tiles)
    print('\n')
    print("Path 3\n")
    print_tiles(path_tiles)
