user_ratings = {}
avg_user_rating = 0

# Add a new rating for a user
def add_rating(user, rating):
    user_ratings[user] = rating

# Get the rating for a specific user
def get_rating(user):
    return user_ratings.get(user)

# Get the average rating for a user
def get_average_rating(self):
    total = 0
    count = 0
    for rating in user_ratings.values():
        total += rating
        count += 1
    return self.avg_user_rating

