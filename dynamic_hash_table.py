from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def rehash(self):
        
        new_size=get_next_size()
        self.total_elements=0
        old_table=self.hash_table
        self.hash_table=[-1]*new_size
        self.table_size=new_size
        # self.params[-1]=new_size

        # Reinsert all existing elements into the new table
        for slot in old_table:
            if slot==-1:
                continue
            if self.collision_type == "Chain":
                for item in slot:
                    self.insert(item)
            else:
                if slot !=-1:
                    self.insert(slot)

        # self.hash_table = new_table
        pass  # Update the hash table to the new one

    def insert(self, x):
        super().insert(x)
        if self.get_load() >= 0.5:
            self.rehash()


class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def rehash(self):
        new_size=get_next_size()
        self.total_elements=0
        old_table=self.hash_table
        self.hash_table=[-1]*new_size
        self.table_size=new_size
        # self.params[-1]=new_size
        

        # Reinsert all existing elements into the new table
        for slot in old_table:
            if slot==-1:
                continue
            if self.collision_type == "Chain":
                for item in slot:
                    self.insert(item)
            else:
                # self.insert(slot)
                self.insert(slot)

        # self.hash_table = new_table # Update the hash table to the new one

    def insert(self, key):
        super().insert(key)
        if self.get_load() >= 0.5:
            self.rehash()

