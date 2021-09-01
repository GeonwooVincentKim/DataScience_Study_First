import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
# sys.path[1] = str(Path(sys.path[1]).parent)

from get_user_data.friendships import *
from attribute.user_attribute import *

if __name__ == "__main__":
    for i in users:
        find_users(i, users)

    # friendships = {user["id"]: [] for user in users}
    # print(friendships)
    

    # for i in friendships:
    #     find_friends(i, friendships)
    # total_connections = sum(number_of_friends(user) for user in users)
