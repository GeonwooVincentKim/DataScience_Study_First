import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from attribute.user_attribute import *

friendships = {user["id"]: [] for user in users}
print(friendships)

friendship_example = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]


for i, j in friendships_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# for i, j in friendships_pairs:
    # friendships[i].append(j)
    # friendships[j].append(i)
