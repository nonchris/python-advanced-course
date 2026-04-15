import random
import time
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn

progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    SpinnerColumn(style="bar.complete"),
    BarColumn(),
    TextColumn("[bright_green]{task.completed:>.1f}/{task.total} ({task.percentage:>.0f}%)", style="bright_green"),
    TimeRemainingColumn(),
)
task1 = progress.add_task("[bar.complete]Downloading", total=100)

layout = Layout(progress)

with Live(layout, refresh_per_second=10, screen=True):
    while not progress.finished:
        progress.update(task1, advance=random.randint(0, 30))
        time.sleep(0.8)
