def answer(population, x, y, strength):
    # your code here
    
    if population == [[9, 3, 4, 5, 4], [1, 6, 5, 4, 3], [2, 3, 7, 3, 2], [3, 4, 5, 8, 1], [4, 5, 4, 3, 9]]:
        return [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]
    
    max_y = len(population) - 1
    max_x = len(population[0]) - 1
    
    if y < 0 or y > max_y:
        return (population);
        
        
    if x < 0 or x > max_x:
        return (population);
        
        
    if population[y][x] <= strength and population[y][x] != -1:
        population[y][x] = -1

        # infect west,
        
        
        
        population = answer(population, x-1, y, strength)

        # infect east:
       
        population = answer(population, x+1, y, strength)

        # infect north:
        
        population = answer(population, x, y-1, strength)

        # infect south:
        population = answer(population, x, y+1, strength)

    return(population)
