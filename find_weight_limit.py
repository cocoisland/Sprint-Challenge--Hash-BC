'''
Given a package with a weight limit limit and an array arr of 
item weights, implement a function getIndicesOfItemWeights 
that finds two items whose sum of weights equals the weight limit limit. 
'''

def getIndicesOfItemWeights(weights, limit):
    # use item weight as key to dictionary and value as array index
    d ={}
    
    for i in range(len(weights)):
        complement = limit - weights[i]
        if complement in d:
            # later index value i, will always be larger than index value in
            # dictionary
            return [i, d[complement]]
        else:
            # index i value for initial dictionary will always start  small
            d[weights[i]] = i
    
print(getIndicesOfItemWeights([4, 6, 10, 15, 16],21))   
# should print [3, 1]

print(getIndicesOfItemWeights([4, 4],8))   
# should print [1, 0]

print(getIndicesOfItemWeights([12, 6, 7, 14, 19, 3, 0, 25, 40],7))   
# should print [6, 2]

print(getIndicesOfItemWeights([9],  9))   
# should print []