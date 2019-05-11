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
            x = random.randrange(self.rows)
            y = random.randrange(self.cols)

            while (x, y) in list_of_bombs:
                x = random.randrange(self.rows)
                y = random.randrange(self.cols)

            list_of_bombs.append((x, y))

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
        for x in range(self.rows):
            for y in range(self.cols):
                neighbors = (
                    (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                    (x,     y - 1),             (x,     y + 1),
                    (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
                )

                neighbor_bombs = 0

                for neighbor in neighbors:
                    x_neighbor = neighbor[0]
                    y_neighbor = neighbor[1]

                    if (0 <= x_neighbor < self.rows) and (0 <= y_neighbor < self.cols):
                        if self.field[x_neighbor][y_neighbor] == "*":
                            neighbor_bombs += 1

                if self.field[x][y] != "*":
                    self.field[x][y] = str(neighbor_bombs)

    def reset(self, rows=None, cols=None, number_of_bombs=None):
        self.__init__(rows, cols, number_of_bombs)
