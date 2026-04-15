import itertools

from rich.live import Live
from rich.layout import Layout

with Live(layout := Layout(name="root"), refresh_per_second=1, screen=True):
    for i in itertools.count(1):
        layout.update(f"{i} iters")
