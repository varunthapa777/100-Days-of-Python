# TODO : 1. create a class with the constructor

class User:
    # constructor
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    # Creating Method
    def follow(self, user):
        self.following += 1
        user.followers += 1


user1 = User("101", "Varun")
user2 = User("102", "Sidhu")

user1.follow(user2)

print(user1.followers)
print(user2.followers)
print(user1.following)
print(user2.following)
