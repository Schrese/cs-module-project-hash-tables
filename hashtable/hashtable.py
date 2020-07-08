class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.size = 0
        self.contents = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        pass


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        pass


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_prime = 0x100000001b3 
        offset_basis = 0xcbf29ce484222325
        # print(FNV_prime, offset_basis)
        # offset_basis and FNV_prime can use the actual number, but doing it this way gives me some semblance of knowing why they are what they are. They are the hex values of... actually, I'm not sure why they are those numbser still... I thought it was 2^64 ? ... but they don't exactly equal one another?
        hash = offset_basis
        for k in key:
            # This is the "clamping" part
            hash = hash * FNV_prime
            hash = hash ^ ord(k)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381 # according to research, the 5381 seems to be an arbitrary number that can be any number that is prime (BUT I tried and it still works when I use the prime number 97 AND the non-prime number 100). So I'm a bit confused by this
        for k in key:
            hash = (hash * 33) + ord(k) # according to my research, the 33 seems to be used all the time. For some reason it's "faster"? Although I'm not sure why yet?
            # print(k)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        # print(key)
        return self.djb2(key) % self.capacity

    # This is the old get method, but I'm just using it to check if there are contents at an index for the 'put' method
    def checkIfContent(self, key): 
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # print('hello')
        lookup = self.hash_index(key)

        if self.size == 0:
            return None
        
        if self.contents[lookup] is None: 
            return None
        
        else:
            return self.contents[lookup].value

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # newNode = HashTableEntry(key, value)
        # newIndex = self.hash_index(key)
        # self.contents[newIndex] = newNode
        # self.size += 1
        
        # REWORKING FOR DAY 2
        # create a new node and hash it
        # see if there is anything already at that index (use the 'get' method here)
        checking = self.checkIfContent(key)
        keyIndex = self.hash_index(key)
        # print(keyIndex, 'keyIndex from put')
        # print(checking, 'checking in put')
        # if nothing is at that index, create a new linked list with the new node as the 'head' and the 'next' will point to None
        # print(self.size)
        if checking is None:
            # print('omg')
            newNode = HashTableEntry(key, value)
            newIndex = self.hash_index(key)
            self.contents[newIndex] = newNode
            # print(self.contents[newIndex].next)
            newNode.next = None
            self.size += 1
        if self.size >= 0.7 * self.capacity:
            newCap = self.capacity * 2
            self.resize(newCap)
        # if something IS at that index, then iterate through that list to see if that 'key' already exists
        else:
            # check if there is only one element in the list. Or rather checking if the first element in the list is the 
            curNode = self.contents[keyIndex]

            while curNode:
                # If it does exist, then update the value of that node
                if curNode.key == key:
                    curNode.value =  value
                # Otherwise, insert that node at the head of the linked list, be sure to update the 'head' to be the newly inserted node, and set its 'next' pointer to be the old head
                else:
                    oldHead = curNode
                    newNode = HashTableEntry(key, value)
                    self.contents[keyIndex] = newNode
                    newNode.next = oldHead
                    self.size += 1
                curNode = curNode.next


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # indexOfKey = self.hash_index(key)
        # deleted = self.contents[indexOfKey]
        # self.contents[indexOfKey] = None
        # self.size -= 1
        # return deleted

        #REWORKING FOR COLLISION
        
        indexOfKey = self.hash_index(key)
        # print(self.size, 'in delete')
        # If there is no content at this index, then there is nothing to delete
        if self.contents[indexOfKey] is None:
            return None
        # if we find a node with the key as the "head" (just the first one listed at that index) then we decrease the size by one, and change the node to be the next node, and return the key for what was deleted
        elif self.contents[indexOfKey].key == key:
            self.size -= 1
            self.contents[indexOfKey] = self.contents[indexOfKey].next
            return key
        # otherwise, the key wasn't at the head of the linked list
        else:
            # if the current node's 'next' points to None, then it means that it is the only element in the list, and we just need to return because it doesn't match the key input
            if self.contents[indexOfKey].next is None:
                return None

            prevNode = None
            curNode = self.contents[indexOfKey]

            # iterate through linked list and if the key is found somewhere in there, then the previous node needs to point to one past the matching node
            while curNode:
                if curNode.key == key:
                    prevNode.next = curNode.next
                    self.size -= 1
                    return key
                prevNode = curNode
                curNode = curNode.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # print('hello')
        # lookup = self.hash_index(key)
        # if self.size == 0:
        #     return None
        # if self.contents[lookup] is None: 
        #     return None
        # else:
        #     return self.contents[lookup].value

        # REWORKING FOR COLLISION
        # store the current node (which is just the 'head', we're not going to call it that, we're just going to have it be what's returned AT that given index without any searching through the linked list)
        lookup = self.hash_index(key)
        curNode = self.contents[lookup]
        # print(curNode.key, 'from get')
        if self.size == 0: 
            return None
        
        if self.contents[lookup] is None:
            return None

        # As long as the current node isn't 'None', I'll search through the node list. 
        while curNode is not None:
            # if the key at the current index is the same as the key entered, then return the value of that key
            if curNode.key == key:
                return curNode.value
            curNode = curNode.next
            # Otherwise set the current node to the current node's 'next' pointer
        return None
            # If the key wasn't found, return 'could not find this'

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        oldList = [None] * self.capacity
        # Make a new array with double the capacity of the old one
        # Have the hash table refer to that new array
        self.contents = self.contents + oldList
        # print(len(self.contents))
        # Run through all the nodes in the old hash table array'
        self.capacity = new_capacity
        # print(self.capacity)
        for i in range(self.capacity):
            entry = self.contents[i]
            # print(i, entry, 'in resize')
            if entry is not None:
                curNode = self.contents[i]
                while curNode:
                    # print(self.contents[i].key, 'key')
                    self.delete(self.contents[i].key)
                    # Put them in the new hash table array
                    self.put(curNode.key, curNode.value)
                    curNode = curNode.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
