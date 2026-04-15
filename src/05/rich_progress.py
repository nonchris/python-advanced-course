import time
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

progress = Progress(
    "[progress.description]{task.description}",
    SpinnerColumn(style="red"),
    BarColumn(),
    TextColumn("{task.percentage:>3.0f}%")
)
task1 = progress.add_task("[red]Downloading...", total=1000)
task2 = progress.add_task("[green]Processing...", total=1000)
task3 = progress.add_task("[cyan]Cooking...", total=1000)

layout = Layout(progress)

with Live(layout, refresh_per_second=10, console=console):
    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)
