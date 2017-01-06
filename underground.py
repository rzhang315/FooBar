#mem_graphs = {}
mem_counts = {}
mem_choose = {}

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

#@memoize  
#def possible_graphs(n, k):
    """
    Returns the total number of graphs with that can be formed using
    n nodes and k vertices. This includes graphs that are
    identical for undirected labelled graphs, as well as
    unconnected graphs.
    This function effectively returns the number of ways you can
    choose k vertices out of the 'n choose 2' possible choices.
    """
#    return choose(n * (n - 1) >> 1, k)
    


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
        # Cayley's formula
        c = int(n ** (n - 2))
    else:
        
        # number of possible vertices
        p = n * (n - 1) >> 1

        if k == p:
            # only way is to connect each node to all other nodes,
            # therefore only a single distinct graph
            c = 1

        else:

            # initially all possible graphs
            c = choose(p, k)

            # there can only be duplicates or unconnected components
            # if the number of nodes is less than p - n + 2.
            # equivalent of k < (n - 1 choose 2)
            if k < p - n + 2:

                for i in range(1, n):
                    x = choose(n - 1, i - 1)

                    # minimum of possible vertices for 'i' nodes and 'k'
                    y = min(i * (i - 1) >> 1, k)

                    for j in range(i - 1, y + 1):
                        # exclude invalid graphs from the total
                        c -= x * choose((n - i) * ((n - i) - 1) >> 1, (k - j)) * count(i, j)

    return c
        
def answer(n, k):
    return count(n,k)
        
    
