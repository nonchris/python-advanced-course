from rich import print
from rich.layout import Layout
from rich.table import Table
from rich.panel import Panel
layout = Layout()
layout.split_column(
    Layout(name="upper", size=3),
    Layout(name="lower")
)
layout["lower"].split_row(
    Layout(name="left", ratio=25),
    Layout(name="right", ratio=75),
)

print(layout)

# Add content to the upper layout
layout["upper"].update(Panel("[bold red]Title: My Project[/bold red]", border_style="red"))

# Add content to the left layout
layout["left"].update(Panel("[green]Whats next[/green]", border_style="green"))

# Create a table for the right layout
table = Table(title="Some Data", expand=True)
table.add_column("Header 1", justify="left", style="cyan")
table.add_column("Header 2", justify="left", style="magenta")

# Add rows to the table
table.add_row("Row 1 Col 1", "Row 1 Col 2")
table.add_row("Row 2 Col 1", "Row 2 Col 2")

# Add the table to a panel
table_panel = Panel(table, border_style="blue", title="Data")

layout["right"].update(table_panel)


print(layout)