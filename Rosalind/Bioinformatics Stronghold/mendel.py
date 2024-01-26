try:

    #PR(A) = PR(X = BLUE and Y = BLUE) + PR(X = RED and Y = BLUE)

    k = 2 # YY
    m = 2 # Yy
    n = 2 # yy

    population =  k + m + n
    dominant_percentage = ((k + m) / population) * 100

    print(dominant_percentage)


    input()

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


#      6.66666%        13.3333333%         13.3333333%
#    YY x YY           YY x Yy             YY x yy

#      Y     Y           Y    Y             Y     Y
#   |-----|-----|     |-----|-----|      |-----|-----|
# Y | YY  | YY  |   Y |  YY | YY  |    y |  Yy |  Yy |
#   |-----|-----|     |-----|-----|      |-----|-----|
# Y | YY  | YY  |   y |  Yy |  Yy |    y |  Yy | Yy  |
#   |-----|-----|     |-----|-----|      |-----|-----|
                                                            #                ADDING THE PERCENT CHANCES UP WE GET OUR MISSING 0.45!!!!
# 100% dom               100% dom             100% dom


#     5%                  6.6666666%
#    Yy x Yy           Yy x yy             yy x yy

#      Y     y           Y    y             y     y
#   |-----|-----|     |-----|-----|      |-----|-----|
# Y | YY  | Yy  |   y |  Yy | yy  |    y |  yy |  yy |
#   |-----|-----|     |-----|-----|      |-----|-----|
# y | Yy  | yy  |   y |  Yy |  yy |    y |  yy | yy  |
#   |-----|-----|     |-----|-----|      |-----|-----|

# 75% dom / 25% rec     50% dom / 50% rec        100% rec

# When calculating the overall probability, consider the different combinations of
# parent organisms and how likely each combination is in the population.
# The probability of dominance in the offspring should reflect the combined likelihood
# of all possible parent combinations.



# The probability of having a dominant allele in the offspring when
# two organisms are randomly selected is a combination of the probabilities of each possible combination.

# You mentioned the percentages for each Punnett square,
# so let's think about how you would combine those percentages
# when considering the likelihood of each parent combination in the population.
