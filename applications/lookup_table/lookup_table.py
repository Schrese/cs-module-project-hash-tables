# Your code here
import random
import math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

cache = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # So... the power is what I need to actually pay attention to (not the x and y). Because several combinations can make the same power. So we're trying to cut down on the amount of time it takes to do the factorial and below
    # cache = {}
    v = math.pow(x, y)
    if v not in cache:
        cache[v] = math.factorial(v)
        cache[v] //= (x + y)
        cache[v] %= 982451653
    return cache[v]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
