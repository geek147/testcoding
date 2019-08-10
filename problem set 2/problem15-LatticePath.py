from math import factorial

#a,b  is grid size axb

#lattice path can be solve with combination which can solbe with binomial coeffiecient 
#binomial coeeficient formula = (a+b)!/a!b!

def latticePath(a,b):

    return int(factorial(a+b)/(factorial(a)*factorial(b)))


#change the value here    

print("number of lattice path: " + str(latticePath(20,20)))