#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(length):
        key = tickets[i].source
        if key != "NONE":
            value = tickets[i].destination
            hash_table_insert(hashtable, key, value)
         
    # start node not in destination list.
    destination_list = []
    for i in range(length):
        destination_list.append(hash_table_retrieve(hashtable, tickets[i].destination))

    # start node
    for i in range(length):
        if tickets[i].source not in destination_list:
            start_node = tickets[i].source
        
    i=0
    route[i] = start_node
    while hash_table_retrieve(hashtable, start_node) is not None:
        i += 1
        next_node = hash_table_retrieve(hashtable,start_node)
        route[i] =next_node
        start_node = next_node

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

#expected = ["PDX", "DCA", "NONE"]
reconstruct_trip(tickets, 3)