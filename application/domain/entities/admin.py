from domain.value_objects.password import Password
class Admin:
    def __init__ (self,password: Password):
        self.password = password
    def system_off(self,error):
        if error == 3:
            raise ValueError("Программа остановилась. Все попытки входа в систему были исчерпаны.")