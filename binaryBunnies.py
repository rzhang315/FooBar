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


class BST:

    def __init__(self, *values):
        self.root = None
        self.left = None
        self.right = None

        for value in values:
            self.insert(value)

    def insert(self, value):
        if not self.root:
            self.root = value

        elif value < self.root:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)

        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)

def count(root):
    if root is None:
       return 0
    else:
       return 1 + count(root.left) + count(root.right)
            
# permutation of the the left side and right side of the tree while the tree remain the same 
# in other word, how many N choose K ways of arranging the order to remain the same.
def input_permutations(tree):
    if not tree:
        return 1

    ls = count(tree.left)
    rs = count(tree.right)
    lp = input_permutations(tree.left)
    rp = input_permutations(tree.right)

    return choose(ls + rs, rs) * lp * rp


def answer(seq):
    return input_permutations(BST(*seq))
