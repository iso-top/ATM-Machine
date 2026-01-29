from application.domain.value_objects.number_card import Number_card
from application.domain.value_objects.pincode import Pincode
from ui.user_menu import user_menu
#библиотека для эффектов в консоль
from rich.console import Console
from time import sleep
console = Console()


def main_menu(account_repo,transaction_repo):
    console.print("[bold #61cf5a]Добро пожаловать в ATM_machine: [/]")
    """Выбор режима."""
    while (True):    
        mode = console.input("[bold #61cf5a]→ Выберите режим [1] User [2] Admin: [/]")
        console.print(f"Вы выбрали: {mode}", style="#61cf5a")
        if mode == "1":
            mode = console.input("[bold #61cf5a]Создать счет [1] Ввести действующий [2] Вернуться назад [3]: [/]")
            if mode == "3":
                continue
            while(True):
                if mode == "1":
                    break
                elif mode == "2":
                    number = "97888772396700"
                    pin = "1772"
                    try:
                        #number = console.input("[bold #61cf5a]Введите номер карточки: ")
                        #pin = console.input("[bold #61cf5a]Введите pincode карточки: ", password=True)
                        
                        with console.status("[bold #61cf5a]Проверяем наличие счета..."):
                            sleep(2)
                            card_vo = Number_card(number)
                            pin_vo = Pincode(pin)
                            account = account_repo.get_by_card(card_vo)
                        console.print("[bold #61cf5a]✔ Счет найден[/]")
                        user_menu(account,account_repo,transaction_repo)
                    except Exception as e:
                        print(f"Ошибка: {e}") # Это покажет, что именно сломалось
                        console.print("[red]✖ Счет не найден[/]")
                        break
                else:
                    console.print("[bold #61cf5a]Неверный выбор[/]")
                    continue
        elif mode == "2":
            pass
        else:
            console.print("[bold #61cf5a]Неверный выбор[/]")
            continue


#61cf5a