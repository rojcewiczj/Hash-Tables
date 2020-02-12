# '''
# Linked List hash table key/value pair
# '''
import hashlib 

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
​
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)
    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
​
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass
    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity
    def insert(self, key, value):
        '''
        Store the value with the given key.
​
        Hash collisions should be handled with Linked List Chaining.
​
        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            # add to the head of the list
            new_node = LinkedPair(key, value)
            new_node.next = self.storage[index]
            self.storage[index] = new_node
            print(f"warning: collision at {index}")
            return
        else:
            self.storage[index] = LinkedPair(key, value)
            return
    def remove(self, key):
        '''
        Remove the value stored with the given key.
​
        Print a warning if the key is not found.
​
        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        prev = None

        if current.key == key:
             self.storage[index] = current.next
        if current.key != key:
            while current.next is not None:
                prev = current
                current = current.next
                if current.key == key:
                   prev.next = current.next
                   return  None
            print (f"WARNING: Key {key} not found")      
      
           



        # if self.storage[index] is not None:
        #     if self.storage[index][0] == key:
        #         old_item = self.storage[index]
        #         self.storage[index] = None
        #     else:
               
        # else:
        #     print(f"WARNING: key {key} not found")
      
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
​
        Returns None if the key is not found.
​
        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        if current is None:
            return None
        elif current.key == key:
            return current.value
        elif current.key !=  key:
            while current.next is not None:
                current = current.next
                if current.key == key:
                   return current.value
            return None
        
    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
​
        Fill this in.
        '''
        old_storage = self.storage
        print(old_storage)
        self.capacity *= 2
        self.storage = [None] * self.capacity  # None 16x in an array
        current_item = None
        for item in old_storage:
            # if item is not None:
            current_item = item
                #  if current.next is None:
                #      self.insert(item.key, item.value)
                #  else:
            while current_item is not None:
                self.insert(current_item.key, current_item.value)
                current_item = current_item.next





if __name__ == "__main__":
    ht = HashTable(2)
 
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.remove('line_1')
    


    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # print("")
