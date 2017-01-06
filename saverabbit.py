def memoize(f):
    
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)
    

            
def answer(food, grid):

    @memoize    
    def reach(t, i, j):
        t -= grid[i][j]
        if i < 0 or j < 0 or t < 0:
            return food + 1
        elif i == j == 0:
            return t
        else:
            return min(reach(t, i - 1, j), reach(t, i, j - 1))

    remainder = reach(food, len(grid) - 1, len(grid) - 1)
    remainder = remainder if remainder <= food else -1
    return remainder
