class User:

    """We store name and birthday"""

    def __init__(self, full_name, birthday):

        self.name = full_name
        self.birthday = birthday 

        # Extract first and last name
        num_pieces = full_name.split(" ")
        self.first_name = num_pieces[0]
        self.last_name = num_pieces[1]



user = User("Dave Floppy", "19740504")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)

help(User)