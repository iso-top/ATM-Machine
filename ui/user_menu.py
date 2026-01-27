"""Работа программы в зависимости от режима."""
from time import sleep
from rich.console import Console
from rich.table import Table

console = Console()
def user_menu(number_card,pin):
    console.print("[bold #61cf5a]✔ Счет найден[/]")
    table = Table(title="Выберите действие")
    
    table.add_column("Действие", style="cyan", no_wrap=True)
    table.add_column("Описание", style="magenta")

    table.add_row("Просмотр баланса счета", "Высветиться ваш текущий баланс")
    table.add_row("Снятие денег со счета", "Вас попросят ввести сумму для списания с вашего баланса, число списания не должно превышать число вашего баланса")
    table.add_row("Пополнение счета", "Вас попросят ввести сумму для пополнения вашего баланса")
    table.add_row("Просмотр истории операций", "Программа выдаст список хранящий в себе историю всех ваших списаний и пополнений")
    console.print(table, justify="left")
    console.input()
