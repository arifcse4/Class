class User():
    def __init__(self, first_name, last_name, *others_info):
        self.first_name = first_name
        self.last_name = last_name
        self.others = others_info
        self.password1 = others_info[-1]
        self.loging_attempt = 0

    def describe_user(self):

        fullName = self.first_name + self.last_name

        print('Name and Address:')
        print(fullName.title())

        for other in self.others:
            if other == self.others[-2]:
                print(other.title())
                break
            print(other.title(), end=', ')
        
        print(f"Value of loging attempt: {str(self.loging_attempt)}")
        self.reset_loging_attempt()
    
    def greed_user(self):
        fullName = self.first_name + ' ' + self.last_name
        print(f'Hello {fullName.title()}!!!')

    def increment_login_attempts(self):
        self.loging_attempt += 1

    def loging(self):
        password2 = input("Enter your password: ")
        
        if password2 == self.password1:
            self.increment_login_attempts()
            self.describe_user()
            self.greed_user()
        elif self.loging_attempt < 3:
            print("Enter correct password!!!")
            self.increment_login_attempts()
            self.loging()
        else:
            self.reset_password()
    
    def reset_password(self):
        ln = input("Enter your last name: ")
        dis = input("Enter your district name: ")

        if ln == self.last_name and dis == self.others[-2]:
            self.password1 = input("Enter new password: ")
            print("Your password has been reseted. Now enter your password.")
            self.reset_loging_attempt()
            self.loging()

    def reset_loging_attempt(self):
        self.loging_attempt = 0
        print(f"Reset loging attempt to {str(self.loging_attempt)}")

user = User('md.', 'uzzal', 'pakshia', 'kalukhali', 'rajbari', 'uzzal@1234')
user.loging()
