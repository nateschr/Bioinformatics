try:

    #PR(A) = PR(X = BLUE and Y = BLUE) + PR(X = RED and Y = BLUE)

    k = 2 # YY
    m = 2 # Yy
    n = 2 # yy

    population =  k + m + n


except Exception as e:
    print(e)


##5. Multiply Probabilities:
##Multiply the probabilities along each path to find the probability of a specific genotype in the offspring.
##
##Example: Probability of offspring being Aa = (1/3) * (1/3) = 1/9 (11.11%)
##
##6. Sum Probabilities:
##Sum the probabilities of all paths leading to the same genotype to get the overall probability of that genotype.
##
##Example: Probability of offspring being Aa = (1/9) + (1/9) + (1/9) = 3/9 = 1/3 (33.33%)
