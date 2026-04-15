from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.columns import Columns
from rich.layout import Layout
from rich.text import Text
import time


class Clock:
    def __init__(self):
        self.start_time = time.time()

    def __rich__(self) -> Panel:
        elapsed_time = time.time() - self.start_time
        seconds = int(elapsed_time)
        milliseconds = int((elapsed_time - seconds) * 1000)

        return Panel(f"{seconds}.{milliseconds}s", title="Time Since Startup")


def get_demo_panel():
    demo_text = Text("This is a demo text panel.", style="bold green")
    return Panel(demo_text, title="Demo Text Panel")


if __name__ == "__main__":
    clock = Clock()

    layout = Layout()
    layout.split_row(
        Layout(get_demo_panel(), name="left"),
        Layout(clock, name="right")
    )

    i = 0
    with Live(layout, refresh_per_second=1, screen=True):
        i += 1
        while True:
            # time.sleep(0.1)
            layout["left"].update(Panel(Text(f"{i} iters")))
            i += 1
