import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from attribute.user_attribute import *


# import timeit
# from main import *

# start_time = timeit.default_timer()

# users = [
#     {"id": 0, "name": "Hero"},
#     {"id": 1, "name": "David"}
# ]

for i in users:
    print("id : {0}".format(i["id"]))
    print("name : " + i["name"])
    print("\n")

# # for user in users:
#     # user["friends"] = []
#     # print(user["friends"])


# friendships = [
#     (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
#     (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
# ]

# # for i in friendships:
# #     print("me: {0}".format(i))
# #     print("friends: {0}".format(friendships[:]))
# #     print("--------------------")


# # friendships = {user["id"]: [] for user in users}


# def find_friends(i, friendships):
#     # friends = friendships[i]

#     for i in friendships:
#         print("friends: {0}".format(i))
#         # print("me : {0}".format(friendships[:]))

#     # return friends[i]


def find_users(i, users):
    for i in users:
        print("users: {0}".format(i))
    
    friendships = {user["id"]: [] for user in users}
    print(friendships)

    for i in friendships:
        if friendships == "\0":
            print("i -> {0} -- user[friends] -> {1}".format(i, friendships))
            # return friendships
        
        else:
            print("Not Null")
            return 0

#     return friendships
#     # for i in user["friends"]:
#     #     if user["friends"] == "":
#     #         print("i -> {0} -- user[friends] -> {1}".format(i, user["friends"]))
#     #         return user["friends"]

#     #     else:
#     #         print("Not Null")
#     #         return 0


# def number_of_friends(user):
#     user_id = user["id"]
#     friend_ids = friendships[user_id]
#     return len(friend_ids)

# friendships = {
#     user["id"]
# }
