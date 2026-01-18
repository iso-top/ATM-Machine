class Password:
    def __init__(self,value: str):
        if not isinstance(value, str):
            raise ValueError("The card's pin code should not be of type int")

        lenght = len(value)
        if lenght < 8:
            raise ValueError("the entered pincode cannot be less than 4 characters")
        