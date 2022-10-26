class User:
    def __init__(self,name,password,phone):
        self.name = name
        self.__password = password
        self.__phone = phone

    def __get_password(self):
        print(self.__password)

    def user_login(self,name,password):
        if(name == self.name and password == self.__password):
            return True
        return False
ryan = User('Ryan Dal', 'NOIHB' ,'0198787564')
# print(ryan.__password)
# print(ryan.__phone)
# ryan.__get_password()
result = ryan.user_login('Ryan Dal', 'NOIHB')
print(result)