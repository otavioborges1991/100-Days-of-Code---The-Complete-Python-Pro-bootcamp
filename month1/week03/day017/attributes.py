class User:

    def __init__(self, user_id: str,username : str):
        self.id = user_id
        self.username = username.lower()
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1
        print(f'{self.username} started following {user.username}')
    
    def unfollow(self, user):
        user.followers -=1
        self.following -=1
        print(f'{self.username} stoped following {user.username}')

    
    



user_1 = User('001', 'Angela')
user_2 = User('002', 'Jack')
user_3 = User('003', 'Janna')
user_1.follow(user_2)
user_1.follow(user_3)
user_2.follow(user_3)

print(f'{user_1.username} has {user_1.followers} followers, and is following {user_1.following}')
print(f'{user_2.username} has {user_2.followers} followers, and is following {user_2.following}')
print(f'{user_3.username} has {user_3.followers} followers, and is following {user_3.following}')

user_3.unfollow(user_1)
print(f'{user_3.username} has {user_3.followers} followers, and is following {user_3.following}')



