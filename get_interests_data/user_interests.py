import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__name__))))))
# sys.path.insert(0, 'E:/Project/Python/Python_DataScience/Project_01_DataScience')
sys.path.insert(0, "E:/DataScience_밑바닥데이터사이언스")

from collections import defaultdict
from attribute.interests_attribute import *
from get_user_data.count_friends import *
from get_user_data.recommand_user import *


user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
    print(user_ids_by_interest)
    
interests_by_user_id = defaultdict(list)

print("\n---------------------------------------------------------------------------------------------------------\n")

for usreS_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

    print(interests_by_user_id)
    

print("\n---------------------------------------------------------------------------------------------------------\n")

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        
        if interested_user_id != user["id"]
    )

print(most_common_interests_with(user) for user in users)
