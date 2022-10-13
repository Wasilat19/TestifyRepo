class User:
    __password = "Password"

    def get_password(self):
        return self.__password

user = User()
print(user.get_password())

class ActiveUser(User):
    def get_password(self):
        return "********"

activeUser = ActiveUser()  
print(activeUser.get_password())      
