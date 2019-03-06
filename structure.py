import random


def get_field(rows, cols, number_of_bombs):
    blank_field = generate_data_structure(rows, cols)
    bombs_places = get_bombs_places(rows, cols, number_of_bombs)
    filled_field = set_bombs_on_structure(blank_field, bombs_places)
    field = calculate_neighborhood(filled_field)

    return field


def generate_data_structure(rows, cols):
    return [[" " for col in range(cols)] for row in range(rows)]


def get_bombs_places(rows, cols, number_of_bombs):
    list_of_bombs = []

    for bomb in range(number_of_bombs):
        x = random.randrange(rows)
        y = random.randrange(cols)

        while (x, y) in list_of_bombs:
            x = random.randrange(rows)
            y = random.randrange(cols)

        list_of_bombs.append((x, y))

    return list_of_bombs


def set_bombs_on_structure(structure, bomb_places_list):
    for bomb in bomb_places_list:
        x = bomb[0]
        y = bomb[1]

        structure[x][y] = "*"

    return structure


def calculate_neighborhood(field):
    number_of_rows = len(field)
    number_of_cols = len(field[0])

    for x in range(number_of_rows):
        for y in range(number_of_cols):
            neighbors = (
                (x-1, y-1), (x-1, y), (x-1, y+1),
                (x,   y-1),           (x,   y+1),
                (x+1, y-1), (x+1, y), (x+1, y+1)
            )

            neighbor_bombs = 0

            for neighbor in neighbors:
                x_neighbor = neighbor[0]
                y_neighbor = neighbor[1]

                if (0 <= x_neighbor < number_of_rows) and (0 <= y_neighbor < number_of_cols):
                    if field[x_neighbor][y_neighbor] == "*":
                        neighbor_bombs += 1

            if field[x][y] != "*":
                field[x][y] = str(neighbor_bombs)

    return field
