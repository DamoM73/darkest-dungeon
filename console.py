from rich.console import Console
from rich.panel import Panel
import time


class UI:
    def __init__(self):
        self.console = Console()

    def display_description(self, description: str):

        self.console.print(Panel(description, style="cyan"))

    def display_action(self, action: str):
        self.console.print(Panel(action, style="yellow"))
        time.sleep(1.5)
