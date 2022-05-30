def read_file(file):
    tiles = []
    with open(file, 'r') as file:
        for line in file:
            tile_line = []
            for number in line:
                if number == '\n':
                    break
                tile_line.append(int(number))
            tiles.append(tile_line)
    return tiles
