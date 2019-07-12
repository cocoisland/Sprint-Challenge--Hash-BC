#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    
    for w in weights:
        if hash_table_retrieve(ht, w) is None:
            hash_table_insert(ht, w, 1)
        else:
            # counting duplicate as value
            value = hash_table_retrieve(ht, w)
            hash_table_insert(ht, w, value+1)

    for i in range(len(weights)):
        target = limit - weights[i]

        if target in weights:
            answer=(None, None)
            j = i

            # find next target that is the same current weight
            if (target == weights[i] and 
                hash_table_retrieve(ht, weights[i]) > 1):
                j = i+1
 
            # find target index in weights
            while j< length and target != weights[j]:
                j += 1
            
            if j > length: 
                # target == weights[j]
                if weights[i] > weights[j]:
                    answer = (str(i), str(j))
                else:
                    answer = (str(j), str(i))
                return(answer)

        # if hash_table_retrieve(ht, target) is not None:
        #     target_value = hash_table_retrieve(ht, target)
        #     if target_value > weights[i]:
        #         answer = (str(target_value), str(weights[i]))
        #     else:
        #         answer = (str(weights[i]), str(target_value))
        # return(answer)
                

    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# print(f' answer2 is {answer_2[0]} {answer_2[1]}')
