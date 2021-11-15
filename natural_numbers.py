def natural_numbers(n):
    """Returnn 1, 2, 3"""
    n = 1
    
    while True:
        yield n
        n += 1
        

for i in natural_numbers(1):
    print("{0}".format(i))
    

