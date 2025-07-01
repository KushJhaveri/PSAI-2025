def staircase(n: int): 
    for stars in range(1, n + 1): 
        spaces = n - stars 
        print(f"{spaces * ' '}{stars * '*'}")

staircase(6)