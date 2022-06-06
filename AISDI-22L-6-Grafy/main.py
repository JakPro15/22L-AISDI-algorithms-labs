from file_reader import read_file
from print_path import show_path, print_tiles
from dijkstra import dijkstra
from sys import argv


def find_zeros(tiles):
    zeros = []
    for x, line in enumerate(tiles):
        for y in range(len(line)):
            if tiles[x][y] == 0:
                zeros.append((x, y))
    return zeros


if __name__ == "__main__":
    if(len(argv) != 2):
        print("The program takes exactly 1 argument.")
    else:
        tiles = read_file(argv[1])
        zeros = find_zeros(tiles)
        path = dijkstra(tiles, zeros[0], zeros[1])
        path_tiles = show_path(tiles, path)
        print_tiles(path_tiles)
 