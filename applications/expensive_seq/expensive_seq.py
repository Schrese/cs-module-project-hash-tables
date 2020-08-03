# Your code here


def expensive_seq(x, y, z):
    # Your code here
    # We need a cache with the key's being 'x, y, z' as a tuple, and the result of them as the value. That way we can look up the tuple before trying to make the math operations. This is a recursive function that is slightly confusing to put into words
    cache = {}
    # We need an inner-function as well (to keep the cache from being global)
    def expensive_inner(x, y, z):
        # If x is less than or equal to zero
        if x <= 0:
            # return y + z
            return y + z
        tup = (x, y, z)
        # If x is greater than 0 and NOT in the cache
        if tup not in cache:
            # create a cache entry that calls the recursion on x, y, and z with the modifications specified in the readme
            cache[tup] = expensive_inner(x-1, y+1, z) + expensive_inner(x-2, y+2, z*2) + expensive_inner(x-3, y+3, z*3)
        # return the cache at that tupple
        return cache[tup]
    # Invoke the inner function on the arguments
    return expensive_inner(x, y, z)



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
