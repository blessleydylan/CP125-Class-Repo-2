def count_bright_spots(pixels):
    bright_spots = 0

    # A bright spot needs two neighbors
    if len(pixels) < 3:
        return 0

    for item in range(1, len(pixels) - 1):
        if pixels[item - 1] < pixels[item] > pixels[item + 1]:
            bright_spots += 1

    return bright_spots
