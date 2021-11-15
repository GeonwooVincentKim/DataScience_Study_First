def apply_to_one(f):
    return f(1)


y = apply_to_one(lambda x: x + 4)
print(y)

tc = int(input())

for i in range(1, tc):
    outer_tc = int(input())
    print(outer_tc)

    for j in range(0, outer_tc):
        inner_tc = map(int, input().split(" "))
        print(inner_tc)
