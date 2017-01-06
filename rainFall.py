def answer(heights):
    
    maxi =  heights.index(max(heights)) 
    
    maxi0 = heights[0:maxi].index(max(heights[0:maxi])) 
    maxi2 = heights[maxi+1:len(heights)].index(max(heights[maxi+1:len(heights)])) 
    maxi2 = maxi+maxi2+1 
    answer = 0
    answer += findBtwAB(maxi0, maxi, heights) #index 
    answer += findBtwBC(maxi, maxi2, heights)

    #print answer 
    return answer
    
    
    
    
def findBtwAB(start, end, heights):
    if (end == 0) or (end == 1):
      return 0

    thresh = min (heights[start], heights [end])
    count = 0
    
    for x in range(start, end+1):
      if (thresh-heights[x])>0:
         count += (thresh-heights[x])

    maxi =  start 
    
    if (maxi == 0):
       return count
    maxi0 = heights[0:maxi].index(max(heights[0:maxi])) 
    count += findBtwAB(maxi0, maxi, heights) 
         
    #print "countAb", count 
    return count
    
    
def findBtwBC(start, end, heights):
    
    if (start == (len(heights)-1)) or (start == (len(heights)-2)):
      return 0

    thresh = min (heights[start], heights [end])
    count = 0
    temp = 0
    for x in range(start, end+1):
      if (thresh-heights[x])>0:
         count += (thresh-heights[x])
    
    maxi = end 
    
    if (maxi == (len(heights)-1)):
      return count
    maxi2 = heights[maxi+1:len(heights)].index(max(heights[maxi+1:len(heights)])) 
    maxi2 = maxi+maxi2+1


    count += findBtwBC(maxi, maxi2, heights)
    #print "countBC", count 
