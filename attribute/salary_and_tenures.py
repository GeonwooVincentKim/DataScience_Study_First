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


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    
    elif tenure < 5:
        return "between two and five"

    else:
        return "more than five"


salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
    # print(salaries_and_tenures)

# Key -> Section of Consecutive Years
# Value -> Users average annual-income of that section
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

print("Dictionary of `Average_salary_bucket` -> {0}".format(average_salary_by_bucket))


# Contains the users average vacation days of annual-year
salaries_and_tenures_and_vacations_list = [
    (83000, 8.7, 5.2), (88000, 8.1, 5),
    (48000, 0.7, 4.8), (76000, 6, 5.4),
    (69000, 6.5, 7.5), (76000, 7.5, 3.8),
    (60000, 2.5, 9.4), (83000, 10, 7.8),
    (48000, 1.9, 6.8), (63000, 4.2, 9.2)
]

for i in salaries_and_tenures_and_vacations_list:
    print(i)


def vacation_bucket(vacation):
    if vacation < 3:
        return "You have no enough vacation days on your annual-life"

    elif vacation < 5:
        return "You should have to spend more time with your family and you"

    elif vacation < 8: 
        return "You doing great job, but remeber not to forget to spend the time with your family"

    else:
        return "You doing perfectly in your life!!!"


salary_by_tenure_and_vacation = defaultdict(list)

for salary, tenure, vacation in salaries_and_tenures_and_vacations_list:
    average_vacation = vacation_bucket(vacation)
    salary_by_tenure_and_vacation[salary].append(salary)

average_salary_by_vacation = {
    vacation_bucket: len(vacation)
    for vacation_bucket, vacation in salary_by_tenure_and_vacation.items()
}

print("Dictionary of `Average_salary_by Vacation` -> {0}".format(average_salary_by_vacation))


def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    
    elif years_experience < 0.5:
        return "unpaid"
    
    else:
        return "paid"


print("Check some First-User paid -> {0}".format(predict_paid_or_unpaid(tenure)))
