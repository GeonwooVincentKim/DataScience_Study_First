import os
import sys
sys.path.insert(0, "E:/DataScience_밑바닥데이터사이언스")
# sys.path.insert(0, 'E:/Project/Python/Python_DataScience/Project_01_DataScience')

from collections import defaultdict

salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]

# Print all of list element of `salaries_and_tenures` list.
for i in salaries_and_tenures:
    print(i)

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len (salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print("Dictionary of `Average_salary_by_Tenure` -> {0}".format(average_salary_by_tenure))
