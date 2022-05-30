def show_path(tiles, path):
    path_tiles = [[" " for tile in line] for line in tiles]
    for point in path:
        path_tiles[point[1]][point[0]] = tiles[point[1]][point[0]]
    return path_tiles


def print_tiles(tiles):
    for line in tiles:
        line_str = ""
        for tile in line:
            line_str += str(tile)
        print(line_str)
