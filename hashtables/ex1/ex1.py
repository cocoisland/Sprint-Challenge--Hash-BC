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
    # duplicate will be overwritten with latest index
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)


    # for w in weights:
    #     print(f' ht: {hash_table_retrieve(ht,w)}')


    for i in range(len(weights)):
        target = limit - weights[i]
        if hash_table_retrieve(ht, target) is not None:
            target_index = hash_table_retrieve(ht, target)

            if target_index > i:
                answer = (str(target_index), str(i))
            else:
                answer = (str(i), str(target_index))
            return answer

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print_answer(answer_2)

