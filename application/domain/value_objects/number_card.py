class Number_card:
    def __init__(self,value: str):
        if not isinstance(value, str):
            raise ValueError("Card number value object")
        
        if not value.isdigit():
            raise ValueError("Card number must contain only digits")
        
        lenght = len(value)
        if lenght > 19:
            raise ValueError("the entered number cannot be more than 19 characters")
        if lenght < 13:
            raise ValueError("the entered number cannot be less than 13 characters")
        
        self.value = value