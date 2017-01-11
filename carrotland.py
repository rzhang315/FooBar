import math

def distance(x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    
    
def getNumPosLine(Ax, Bx, Ay, By):
        x = abs(Ax - Bx)
        y = abs(Ay - By)
        return ( GCD(x,y) + 1 )
      
    
def GCD( x,  y):
        return x if y == 0 else GCD(y, x%y)
        #return y == 0 ? x : GCD(y, x%y)
    
    
def parallelOrPerpendicular(Ax,  Ay,  Bx,  By):
        return ( (Ax == Bx) or (Ay == By) )
    

def answer(vertices):
    leftBound = min( vertices[0][0], vertices[1][0], vertices[2][0] )
    rightBound = max( vertices[0][0], vertices[1][0], vertices[2][0] )
    lowerBound = min( vertices[0][1], vertices[1][1], vertices[2][1] )
    upperBound = max( vertices[0][1], vertices[1][1], vertices[2][1] )

    horizontalRange = abs(rightBound - leftBound)
    verticalRange = abs(upperBound - lowerBound)

    answer =  ( horizontalRange - 1 ) * ( verticalRange - 1 )
    #print ("anws", answer)

    for poIndex in range(0, 3):
         #   // first po
         Ax = vertices[poIndex][0]
         Ay = vertices[poIndex][1]
            
         #   // second po
         Bx = vertices[(poIndex+1)%3][0]
         By = vertices[(poIndex+1)%3][1]
            
         #   // is line perpendicular or parallel
         #   // to the X-axis
         if(parallelOrPerpendicular(Ax, Ay, Bx, By)): 
                continue
            
            
         numPtsLine = getNumPosLine(Ax, Bx, Ay, By)
            
         #   exclude endpos
         numPtsLine -= 2
            
         width = abs(Ax - Bx)
         height = abs(Ay - By)
            
         num = ( (width - 1) * (height - 1) ) - numPtsLine
            
         answer -= numPtsLine + num/2
        
         #print ("anws", answer)
    for a in range(0, 3): 
            x = vertices[a][0]
            y = vertices[a][1]

            if (x == leftBound or x == rightBound or y == upperBound or y == lowerBound): 
                continue
            

            #// If this po is inside the rectangle, it must mean that
            #// the other two pos are the corners of the rectangle
            edge1 = vertices[(a + 1) % 3]
            edge2 = vertices[(a + 2) % 3]

            #// other two corners
            edge3 = [edge1[0], edge2[1]]
            edge4 = [edge2[0], edge1[1]] 

            #// need to find which corner this po is closer to,
            #// since the contained rectangle is not a part of the triangle.
            distance1 = distance(x, y, edge3[0], edge3[1])
            distance2 = distance(x, y, edge4[0], edge4[1])

            edge = edge3 if (distance1 < distance2) else edge4
            #edge = distance1 < distance2 ? edge3 : edge4

            #// Subtract the double-counted area from the corner
            width = abs(edge[0] - x)
            height = abs(edge[1] - y)

            answer -= width * height
        
            #print ("anws", answer)

    return answer
