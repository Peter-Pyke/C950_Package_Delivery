from Package_Data import loadPackageData, getNumberOfItemsFromMyHash
import  math


# This is my Hash table class and is what I use to hold all my package data
class ChainingHashTable:

    # Constructor for ChainingHashTable class
    def __init__(self, init_capacity=10):
        self.table = []

        for i in range(init_capacity):
            self.table.append([])

    # Insert function takes a key and item and added them to the hash table
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search function takes a key and returns the information about the package object associated with it
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in  bucket_list:
            if kv[0]==key:
                return kv[1]
        return None

    # Remove function takes a key and removes both the key and what is associated with it from the hash
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])



