class Pincode:
    def __init__(self,value: str):
        if not isinstance(value, str):
            raise ValueError("The card's pin code should not be of type int")
        
        if not value.isdigit():
            raise ValueError("Card number must contain only digits")
        
        lenght = len(value)
        if lenght > 4:
            raise ValueError("the entered pincode cannot be more than 4 characters")
        if lenght < 4:
            raise ValueError("the entered pincode cannot be less than 4 characters")