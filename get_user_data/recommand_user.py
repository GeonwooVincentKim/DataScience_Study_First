import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from attribute.user_attribute import *
from get_user_data.new_friendships import friendships


def foaf_ids_bad(user):
    # "foaf" is the abbreviation meaning of "friend of a friend"
    return [
        foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]
    ]

print(foaf_ids_bad(users[0]))
