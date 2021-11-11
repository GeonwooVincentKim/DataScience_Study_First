import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from attribute.user_attribute import *

friendships = {user["id"]: [] for user in users}
print(friendships)