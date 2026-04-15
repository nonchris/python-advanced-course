import sys
import time

from rich import print
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.style import Style

print("[#ffc000]Seeing [bold italic red]Red[/b italic red]!")
style = Style(color="magenta2", bgcolor="bright_cyan", underline=True)
print(Text("Eternal Blue", style=style))
print(f"[{style}]Eternal Blue")

class Counter:
    def __init__(self):
        self.i = 0

    def __rich__(self):
        text = Text(" ".join(f"{i}" for i in range(self.i)), no_wrap=False, style="green")
        panel =  Panel(text, title="Just counting", border_style="yellow")
        self.i += 1
        return panel

layout = Layout(name="root")

layout.split(
    Layout(name="header", size=3),
    Layout(name="body")
)
layout_header = layout["header"]

layout["body"].split_row(
    Layout(name="left", ratio=50),
    Layout(name="mid", ratio=25),
    Layout(name="right", ratio=25)
)
layout_left = layout["left"]
layout_mid = layout["mid"]
layout_right = layout["right"]

header = Table.grid(expand=True)
header.add_column(justify="center")
header.add_row("[green]Just a headline")
layout_header.update(Panel(header, border_style="red"))
lines = ["never", "gonna", "give", "you", "up"]
counter = Counter()
layout_right.update(counter)
print(Panel(header, border_style="red"))
print(Panel(Panel(layout, title="inner"), title="outer"))

# print()
# print(layout)
# with Live(layout, refresh_per_second=1, screen=True, redirect_stderr=False):
#     i = 0
#     while True:
#
#         layout_left.update(Panel(" ".join(lines[0:i]), title="lyrics"))
#
#
#         if i < len(lines):
#             i += 1
#         else:
#             i = 0
#         time.sleep(1)






