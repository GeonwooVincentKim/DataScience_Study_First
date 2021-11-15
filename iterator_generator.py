def generate_range(n):
    i = 0
    
    while i < n:
        yield i
        i += 1
        print(i)


for i in generate_range(10):
    print(f"i: {i}")
