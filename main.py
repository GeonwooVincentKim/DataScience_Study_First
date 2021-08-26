users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "David"}
]

for i in users:
    print("id : {0}".format(i["id"]))
    print("name : " + i["name"])
    print("\n")

for user in users:
    user["friends"] = []
    print(user["friends"])
