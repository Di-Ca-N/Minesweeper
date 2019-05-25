import random


class FieldDataStructure:
    def __init__(self, rows, cols, number_of_bombs):
        self.rows = rows
        self.cols = cols
        self.number_of_bombs = number_of_bombs

        self.bombs_places = self.get_bombs_places()
        self.field = self.generate_blank_field()
        self.place_bombs_on_field()
        self.calculate_bombs_neighborhood()

    def __repr__(self):
        structure_str = ""

        for row in self.field:
            structure_str += "\t"
            structure_str += " ".join(row)
            structure_str += "\n"

        return "FieldDataStructure(\n{})".format(structure_str)

    def __getitem__(self, item):
        return self.field[item]

    def __len__(self):
        return self.cols * self.rows

    def get_bombs_places(self):
        list_of_bombs = []

        for bomb in range(self.number_of_bombs):
            r = random.randrange(self.rows)
            c = random.randrange(self.cols)

            while (r, c) in list_of_bombs:
                r = random.randrange(self.rows)
                c = random.randrange(self.cols)

            list_of_bombs.append((r, c))

        return list_of_bombs

    def generate_blank_field(self):
        field = []
        for i in range(self.rows):
            row = []

            for j in range(self.cols):
                row.append(" ")

            field.append(row)

        return field

    def place_bombs_on_field(self):
        for bomb in self.bombs_places:
            x = bomb[0]
            y = bomb[1]

            self.field[x][y] = "*"

    def calculate_bombs_neighborhood(self):
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = (
                    (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                    (r,     c - 1),             (r,     c + 1),
                    (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
                )

                neighbor_bombs = 0

                for neighbor in neighbors:
                    row_neighbor = neighbor[0]
                    col_neighbor = neighbor[1]

                    if (0 <= row_neighbor < self.rows) and (0 <= col_neighbor < self.cols):
                        if self.field[row_neighbor][col_neighbor] == "*":
                            neighbor_bombs += 1

                if self.field[r][c] != "*":
                    self.field[r][c] = str(neighbor_bombs)

    def reset(self, rows=None, cols=None, number_of_bombs=None):
        self.__init__(rows, cols, number_of_bombs)
