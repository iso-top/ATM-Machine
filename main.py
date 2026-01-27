from infrastructure.persistence.db_connection import DatabaseConnection
from infrastructure.persistence.postgres_account_repository import PostgresAccountRepository

from ui.main_menu import main_menu  # функция для запуска главного меню
from rich.console import Console 
from time import sleep

console = Console()
def main():
    """Подключение к базе данных"""
    try:
        db = DatabaseConnection(
            host="localhost",
            port=5432,
            dbname="atm_machine",
            user="postgres",
            password="postgres"
        )
        with console.status("[bold green]Подключаемся к базе данных...") as status:
            sleep(3)
            conn = db.get_connection()
            account_repo = PostgresAccountRepository(conn)
            console.print("[bold green]✔ Подключение к базе данных прошло успешно[/]")
    except Exception as e:
        console.print("[red]✖ Подключение к базе данных не удалось[/]")
        raise


    # Запуск главного меню
    main_menu(account_repo)  # передаём репозиторий, чтобы UI мог вызывать use cases

if __name__ == "__main__":
    main()
