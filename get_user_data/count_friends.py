import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from collections import Counter
from recommand_user import *


def friends_of_friends(user):
    user_id = user["id"]
    
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )


print(friends_of_friends(users[3]))
