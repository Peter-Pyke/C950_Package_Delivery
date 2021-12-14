from Package_Data import loadPackageData, getNumberOfItemsFromMyHash
import  math
class ChainingHashTable:
    def __init__(self, init_capacity=10):
        self.table = []

        for i in range(init_capacity):
            self.table.append([])

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

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in  bucket_list:
            if kv[0]==key:
                return kv[1]
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])



