from domain.value_objects.password import Password
class Admin:
    def __init__ (self,password,admin_id):
        self.password = password
        self.admin_id = admin_id
    def system_off(self,error):
        if error == 3:
            raise ValueError("The program has stopped. All login attempts have been used up.")