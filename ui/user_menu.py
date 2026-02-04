from rich.console import Console
from rich.table import Table
from ui.user_action import *
from application.use_cases.withdraw_balance import WithdrawBalance
from application.use_cases.deposit_balance import DepositBalance

#Работа программы в зависимости от режима.
console = Console()
def user_menu(account, account_repo,transaction_repo):
    deposit_uc = DepositBalance(account_repo,transaction_repo)
    withdraw_uc = WithdrawBalance(account_repo,transaction_repo)
    while(True):
        table = Table(title="Выберите действие")
        
        table.add_column("Действие", style="cyan", no_wrap=True)
        table.add_column("Описание", style="magenta")

        table.add_row("[1] Просмотр баланса счета", "Высветиться ваш текущий баланс")
        table.add_row("[2] Снятие денег со счета", "Вас попросят ввести сумму для списания с вашего баланса, число списания не должно превышать число вашего баланса")
        table.add_row("[3] Пополнение счета", "Вас попросят ввести сумму для пополнения вашего баланса")
        table.add_row("[4] Просмотр истории операций", "Программа выдаст список хранящий в себе историю всех ваших списаний и пополнений")
        console.print(table, justify="left")
        answer = console.input()

        if answer == "1":
            show_balance(account)
        elif answer == "2":
            update_balance(account,withdraw_uc,"снятия")
        elif answer == "3":
            update_balance(account,deposit_uc)
        elif answer == "4":
            show_transaction(account,transaction_repo)
        else:
            console.print("[bold #61cf5a]Не корректный ввод")
            continue