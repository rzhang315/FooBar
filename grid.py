"""
Reference: http://mathworld.wolfram.com/LightsOutPuzzle.html
http://www.sfu.ca/~jtmulhol/math302/notes/302notes.pdf
"""
import itertools

def lightHouse(N):
    
    #zero = [0 for i in range(N)] # cant do this because 
    # When you use the [x]*n syntax, what you get is a list of n many x objects, but they're all references to the same object.
    
    zeros =  [[0 for i in range(N)] for i in range(N)] 
    I = [zeros[i]*1 for i in range(N)]  #list(zeros)
    for i in range(N):
        I[i][i] = 1
        #print (I)
        #print (zeros)
 
    #print (I)
    C =  [I[i]*1 for i in range(N)]
    #print (C)
    for i in range(N):
      
        if i != N-1: 
            C[i+1][i] = 1
            C[i][i+1] = 1
    
    #print (C)
    A = [[0 for i in range(N**2)] for i in range(N**2)] # [[0]* (N**2)]* (N**2)
    for i in range(N):
        sta = i*N
        end = i*N + N
        k = 0 
        for j in range(sta, end):
            #print (i,j,k,sta,end)
            #print (A[j][sta:end])
            #print (C[k][:])
            A[j][sta:end] = C[k][:]
        
            #print ("part A", A[j][sta:end])
            #print ("A", A)

            if i != N-1: 
            
                A[j+N][sta:end] = I[k][:]
        
                A[j][sta+N:end+N] = I[k][:]
        
            k+=1
    return A

def check_odd_matrix(matrix):
    N = len(matrix)  # Size of the matrix

    #pp = pprint.PrettyPrinter(indent=4)
 
    A = lightHouse(N) # get lightHouse Matrix
    #b = [0]* (N**2)
    #pp.pprint (A)
   
    b = []
    b += (matrix[i] for i in range(N))
    #print (b)
    # need to solve Ax = b, however cant import numpy function. change ways

def answer(matrix):

    N = len(matrix)  
    R = range(N)     

    col_sums = []
    row_sums = []
    for i in R:
        row_sums.append(sum(matrix[i]))
        col_sums.append(sum(matrix[j][i] for j in R))


    def point_parity_sum(matrix):

        S = 0
        P = range(len(matrix))  

        for row in P:
            for col in P:
                S += (row_sums[row] + col_sums[col] - matrix[row][col]) & 1

        return S

    if not N & 1:
        return point_parity_sum(matrix)

    if len(set(x & 1 for x in row_sums + col_sums)) != 1:
        return -1
    
    check_odd_matrix(matrix)
    result = None

    for row in matrix:
        row.append(0)

    for permutation in itertools.product([0, 1], repeat=N):

        if sum(permutation) & 1 != row_sums[0] & 1:
            continue

        col_sums.append(0)
        row_sums.append(0)

        permutation += (0,)

        for i in R:
            col_sums[i] += permutation[i]

        for i in R:

            F = 0
            for j in R:
                F += (row_sums[i] + col_sums[j] - matrix[i][j]) & 1

            flip = 1 if F > N >> 1 else 0

            matrix[i][N] = flip

            if flip:
                row_sums[i] += 1
                col_sums[N] += 1

        matrix.append(permutation)

        row_sums[N] = sum(permutation)

        candidate = point_parity_sum(matrix)

        if candidate < result or result is None:
            result = candidate

        for i in R:
            row_sums[i] -= matrix[i][N]
            col_sums[i] -= matrix[N][i]

        matrix.pop()
        col_sums.pop()
        row_sums.pop()

    for row in matrix:
        row.pop()

    return result
