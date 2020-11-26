class User():
    def __init__(self, first_name, last_name, *others_info):
        self.first_name = first_name
        self.last_name = last_name
        self.others = others_info

    def describe_user(self):
        fullName = self.first_name + self.last_name
        print('Name and Address:')
        print(fullName.title())
        for other in self.others:
            if other == self.others[-1]:
                print(other.title())
                continue
            print(other.title(), end=', ')
    
    def greed_user(self):
        fullName = self.first_name + ' ' + self.last_name
        print(f'Hello {fullName.title()}!!!')

user = User('md.', 'uzzal', 'pakshia', 'kalukhali', 'rajbari')
user.describe_user()
user.greed_user()
