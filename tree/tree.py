class BaseTree:
    def __init__(
        self, top_height, trunk_height, bottom_height, top_simbol, bottom_simbol, trunk_simbol
    ) -> None:
        self.top_height = top_height
        self.bottom_height = bottom_height
        self.trunk_height = trunk_height
        self.top_simbol = top_simbol
        self.bottom_simbol = bottom_simbol
        self.trunk_simbol = trunk_simbol

    def get_last_line_size(self):
        return (self.top_height * 2) - 1

    def get_top(self):
        lst = []
        for x in range(1, self.top_height + 1):
            tree_breek = self.top_simbol * x
            space = " " * (self.top_height - x)
            tree_line = f"{space}{tree_breek}{tree_breek[:x-1]}"
            lst.append(tree_line)
        return lst

    def get_trunk(self):
        size = self.get_last_line_size()
        middle = size // 2
        lst = []
        for _ in range(self.trunk_height, 0, -1):
            tree_breek_size = (size - middle) // 2
            if tree_breek_size % 2 == 0:
                tree_breek_size -= 1
            tree_breek = self.trunk_simbol * tree_breek_size

            middle_of_breek = tree_breek_size // 2
            space = " " * (middle - middle_of_breek)

            tree_line = f"{space}{tree_breek}"
            lst.append(tree_line)

        return lst

    def get_bottom(self):
        size = self.get_last_line_size()
        tree_line = ""
        lst = []

        for x in range(size):
            if x % 2 != 0:
                tree_line += " "
            else:
                tree_line += self.bottom_simbol

        for _ in range(self.bottom_height):
            lst.append(tree_line)

        return lst

    def draw_top(self):
        for x in self.get_top():
            print(x)

    def draw_bottom(self):
        for x in self.get_bottom():
            print(x)

    def draw_trunk(self):
        for x in self.get_trunk():
            print(x)

    def draw(self):
        self.draw_top()
        self.draw_bottom()
        self.draw_trunk()


class Tree(BaseTree):
    def __init__(
        self,
        top_height=10,
        trunk_height=2,
        bottom_height=1,
        top_simbol="*",
        bottom_simbol="'",
        trunk_simbol="|",
    ) -> None:
        super().__init__(
            top_height=top_height,
            trunk_height=trunk_height,
            bottom_height=bottom_height,
            top_simbol=top_simbol,
            bottom_simbol=bottom_simbol,
            trunk_simbol=trunk_simbol,
        )
