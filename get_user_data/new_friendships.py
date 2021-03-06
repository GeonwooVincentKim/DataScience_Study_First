import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from attribute.user_attribute import *

friendships = {user["id"]: [] for user in users}
print(friendships)

for i, j in friendships_pairs:
    # print("Before friendships[i] -> {0}".format(friendships[i]))
    # print("Before friendships[j] -> {0}".format(friendships[j]))
    
    friendships[i].append(j)
    friendships[j].append(i)
    
    print("friendships[i] -> {0}".format(friendships[i]))
    # print(friendships[i])
    print("friendships[j] -> {0}".format(friendships[j]))
    print("\n")

def number_of_friends(user):
    """Check how many friends does `user` have

    Args:
        user (dictionary): Get the id of dictionary of friendships
    """
    user_id = user["id"]
    
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)

num_users = len(users)
average_connections = total_connections / num_users
print(average_connections)

# Generate the list that consist (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(number_of_friends)

show_result = num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],  # Based on num_friends
    reverse=True
)
print(show_result)
