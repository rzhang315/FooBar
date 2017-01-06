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
def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

@memoize   
def count(n, k):

    if k == n - 1:
        c = int(n ** (n - 2))
    else:
        p = n * (n - 1) >> 1

        if k == p:
            # only one way
            c = 1
        else:
            c = choose(p, k)

            if k < p - n + 2: # choose(n - 1, 2): for ex, maybe one unconnected from network
                #find such unconnected sums
                for i in range(1, n):
                    x = choose(n - 1, i - 1)
                    y = min(i * (i - 1) >> 1, k)

                    for j in range(i - 1, y + 1):
                        # formula from https://oeis.org/A001187/a001187.pdf
                        # to calculate number of labeled graphs
                        c -= x * choose((n - i) * ((n - i) - 1) >> 1, (k - j)) * count(i, j)

    return c
        
def answer(n, k):
    return count(n,k)
        
    
