def apply_to_one(f):
    return f(1)


y = apply_to_one(lambda x: x + 4)
print(y)
