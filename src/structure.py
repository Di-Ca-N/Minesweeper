import random


class FieldDataStructure:
    """Manage the data structure used to generate the Minesweeper field"""
    def __init__(self, rows, cols, number_of_bombs):
        self.rows = rows
        self.cols = cols
        self.number_of_bombs = number_of_bombs
        self.field = self.generate_field()

    def __getitem__(self, item):
        return self.field[item]

    def reset_properties(self, rows=None, cols=None, number_of_bombs=None):
        if rows is not None:
            self.rows = rows

        if cols is not None:
            self.cols = cols

        if number_of_bombs is not None:
            self.number_of_bombs = number_of_bombs

        self.field = self.generate_field()

    def generate_field(self):
        blank_field = self.generate_data_structure(self.rows, self.cols)
        self.bomb_places = self.get_bombs_places(self.rows, self.cols, self.number_of_bombs)
        filled_field = self.place_bombs_on_structure(blank_field, self.bomb_places)
        field = self.calculate_neighborhood(filled_field)

        return field

    @staticmethod
    def generate_data_structure(rows, cols):
        return [[" " for col in range(cols)] for row in range(rows)]

    @staticmethod
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

    @staticmethod
    def place_bombs_on_structure(structure, bomb_places_list):
        for bomb in bomb_places_list:
            x = bomb[0]
            y = bomb[1]

            structure[x][y] = "*"

        return structure

    @staticmethod
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
