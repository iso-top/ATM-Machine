class Password:
    def __init__(self,value: str):
        if not isinstance(value, str):
            raise ValueError("Пароль не должен быть типа не строка")

        lenght = len(value)
        if lenght < 8:
            raise ValueError("Пароль должен быть не менее 8 символов")