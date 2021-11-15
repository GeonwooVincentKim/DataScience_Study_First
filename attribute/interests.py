import os
import sys
# sys.path.insert(0, "E:/DataScience_밑바닥데이터사이언스")
# sys.path.insert(0, "E:/Project/Python/Python_DataScience/Project_01_DataScience")
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from collections import Counter
from interests_attribute import interests

words_and_counts = Counter(
    word
    for user, interest in interests
    for word in interest.lower().split() 
)

print(words_and_counts)

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)

    # Will not print this part
    elif count < 1:
        print("Not satisfied condition : {0} {1}".format(word, count))
