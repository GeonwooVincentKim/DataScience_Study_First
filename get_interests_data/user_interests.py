import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__name__))))))
sys.path.insert(0, 'E:/Project/Python/Python_DataScience/Project_01_DataScience')

from collections import defaultdict
from attribute.interests_attribute import *
from get_user_data.count_friends import *
from get_user_data.recommand_user import *


user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
    print(user_ids_by_interest)