from random import choice

from rich.panel import Panel
from rich.table import Table


class DumbBuggySnake:
    def __init__(self, field_size: int, marker_style="[red]X"):
        self.field_size = field_size
        self.reset()
        self.field: list[list[str]]
        self.marker_pos_x = field_size // 2
        self.marker_pos_y = field_size // 2
        self.marker_style = marker_style
        self.next_forbidden_move: tuple[bool, int] | None = None
        self.move_history = []

    def reset(self):
        self.field = [[" "] * self.field_size for _ in range(self.field_size)]
        self.marker_pos_x = self.field_size // 2
        self.marker_pos_y = self.field_size // 2
        self.next_forbidden_move = None

    def add_new_marker(self):
        vertical = choice([True, False])
        offset = choice([-1, 1])

        while self.next_forbidden_move == (vertical, offset):
            vertical = choice([True, False])
            offset = choice([-1, 1])

        if vertical:
            self.marker_pos_y += offset
        else:
            self.marker_pos_x += offset


        if self.field[self.marker_pos_y][self.marker_pos_x] == self.marker_style:
            self.reset()
            return

        self.field[self.marker_pos_y][self.marker_pos_x] = "[red]X"
        self.move_history.append((vertical, offset))
        self.next_forbidden_move = (vertical, offset * -1)

    def __rich__(self):
        self.add_new_marker()
        grid = Table.grid(expand=True)
        grid.add_column(justify="center")
        grid.add_row("\n".join("".join(row) for row in self.field))
        return Panel(grid, title="Dumb Snake", border_style="green")