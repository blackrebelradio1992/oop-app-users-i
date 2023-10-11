# your User class goes here
class User:
    def __init__(self, userName, email, phoneNumber, city):
        self.userName = userName
        self.email = email
        self.phoneNumber = phoneNumber
        self.city = city

    def __str__(self):
        return f"Your Username is {self.userName}, your email is {self.email}, Phone number is {self.phoneNumber} and your city is {self.city}"
    
    



jake = User("jake39", "jake39@mail.com", "312-123-4567",'Thunderdome')

john = User("jj45on", "johnDaDon@mail.com", 123-456-7890, "Valhalla")

print(jake)
print(john)