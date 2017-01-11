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

@memoize 
def R(n):
    if n < 3:
        return [1, 1, 2][n]
    else:
        h = n >> 1
        if n%2 == 1:
            # odd
            return R(h) + R(h - 1) + 1
        else:
            # even
            return R(h) + R(h + 1) + h
            

def binary_search(a, b, target, odd_mid):
    if b <= a:
        return None

    # midpoint
    n = a + ((b - a) >> 1)
    n += odd_mid != n & 1

    S = R(n)
    if S == target:
        return n

    if S > target:
        b = n - 1
    else:
        a = n + 1
    return binary_search(a, b, target, odd_mid)

# return the largest
def answer(str_S):
    s = int(str_S)

    odd = binary_search(0, s, s, 1)
    even = binary_search(0, s, s, 0)
    if odd == None or even == None:
        return even or odd
    else:
        return max(even, odd)
        

