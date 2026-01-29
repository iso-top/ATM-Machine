from time import sleep
from rich.console import Console
from rich.table import Table
from application.use_cases.get_transaction_history import GetTransactionHistory

console = Console()

def show_balance(account): 
    with console.status("[green]Получаем баланс..."):
        sleep(1)
    console.print(f"[bold green]Ваш баланс: {account.balance} ₽[/]")

def update_balance(account, use_case, description="пополнения"):
    amount_str = console.input(f"Введите сумму для {description}: ")

    try:
        amount = int(amount_str)

        with console.status("[bold green]Обработка операции..."):
            use_case.execute(account, amount)
            sleep(1)

        console.print("[bold green]✔ Операция успешно выполнена[/]")
        console.print(f"[bold]Новый баланс: {account.balance} ₽[/]")

    except ValueError as e:
        console.print(f"[red]✖ Ошибка: {e}[/]")
    except Exception as e:
        console.print(f"[red]✖ Неизвестная ошибка: {e}[/]")


def show_transaction(account, transaction_repo):
    console.print("[bold green]История операций[/]")

    # Создаем Use Case
    use_case = GetTransactionHistory(transaction_repo)

    with console.status("[bold green]Загружаем историю..."):
        sleep(1)
        transactions = use_case.execute(account.account_id)

    if not transactions:
        console.print("[yellow]История операций пуста[/]")
        return

    table = Table(title=f"История операций (Счет: {account.number_card.value})")

    table.add_column("Дата", style="cyan")
    table.add_column("Тип", style="magenta")
    table.add_column("Сумма", justify="right")

    for tx in transactions:
        color = "green" if tx.type == "DEPOSIT" else "red"
        
        table.add_row(
            tx.timestamp.strftime("%Y-%m-%d %H:%M"),
            tx.type,
            f"[{color}]{tx.amount} ₽[/]"
        )

    console.print(table)