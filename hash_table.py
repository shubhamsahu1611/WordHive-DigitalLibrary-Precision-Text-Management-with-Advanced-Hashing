from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        self.collision_type = collision_type
        self.params = params
        self.total_elements = 0
        self.hash_table = -1
        self.table_size = -1
        if collision_type == "Chain":
            self.table_size = params[1]
            self.hash_table = [-1 for _ in range(self.table_size)]  # List of lists for chaining
        elif collision_type == "Linear" or collision_type == "Double":
            self.table_size = params[-1]  # Use the last parameter as table size
            self.hash_table = [-1] * self.table_size  # List for linear probing or double hashing

    def character_assignment(self, letter):
        if 'a' <= letter <= 'z':
            return (ord(letter) - ord('a'))
        else:
            return (ord(letter) - ord('A') + 26)

    def primary_Hash_Function(self, key, z, Mod):
        hash_value = 0
        k = 1
        for char in key:
            assign_value = self.character_assignment(char)
            hash_value = (hash_value + assign_value * k) % Mod
            k = (k * z) % Mod
        return hash_value % Mod

    def secondary_Hash_Function(self, key, z2, c2):
        hash_value = 0
        k = 1
        for char in key:
            assign_value = self.character_assignment(char)
            hash_value = (hash_value + assign_value * k) % c2
            k = (k * z2) % c2
        return c2 - (hash_value % c2)

    def insert(self, x):
        if isinstance(x, tuple):
            key, value = x
            hash_value = self.primary_Hash_Function(key, self.params[0], self.table_size)
            if self.collision_type == "Chain":
                current_chain = self.hash_table[hash_value]
                if current_chain == -1:
                    current_chain = []
                    current_chain.append((key, value))
                    self.total_elements += 1
                else:
                    found = False
                    for entry in current_chain:
                        if entry[0] == key:
                            found = True
                    if not found:
                        current_chain.append((key, value))
                        self.total_elements += 1
                self.hash_table[hash_value] = current_chain

            elif self.collision_type == "Linear":
                linear_index = hash_value
                while True:
                    if self.hash_table[linear_index] == -1 or self.hash_table[linear_index][0] == key:
                        if self.hash_table[linear_index] == -1:
                            self.hash_table[linear_index] = (key, value)
                            self.total_elements += 1
                        return
                    else:
                        linear_index = (linear_index + 1) % self.table_size
                    if linear_index == hash_value:
                        return

            else:
                double_index = hash_value
                gap = self.secondary_Hash_Function(key, self.params[1], self.params[2])
                while True:
                    if self.hash_table[double_index] == -1 or self.hash_table[double_index][0] == key:
                        if self.hash_table[double_index] == -1:
                            self.hash_table[double_index] = (key, value)
                            self.total_elements += 1
                        return
                    else:
                        double_index = (double_index + gap) % self.table_size
                    if double_index == hash_value:
                        return
        else:
            key = x
            hash_value = self.primary_Hash_Function(key, self.params[0], self.table_size)
            if self.collision_type == "Chain":
                current_chain = self.hash_table[hash_value]
                if current_chain == -1:
                    current_chain = []
                    current_chain.append(key)
                    self.total_elements += 1
                else:
                    found = False
                    for entry in current_chain:
                        if entry == key:
                            found = True
                    if not found:
                        current_chain.append(key)
                        self.total_elements += 1
                self.hash_table[hash_value] = current_chain

            elif self.collision_type == "Linear":
                linear_index = hash_value
                while True:
                    if self.hash_table[linear_index] == -1 or self.hash_table[linear_index] == key:
                        if self.hash_table[linear_index] == -1:
                            self.hash_table[linear_index] = key
                            self.total_elements += 1
                        return
                    else:
                        linear_index = (linear_index + 1) % self.table_size
                    if linear_index == hash_value:
                        return

            else:
                double_index = hash_value
                gap = self.secondary_Hash_Function(key, self.params[1], self.params[2])
                while True:
                    if self.hash_table[double_index] == -1 or self.hash_table[double_index] == key:
                        if self.hash_table[double_index] == -1:
                            self.hash_table[double_index] = key
                            self.total_elements += 1
                        return
                    else:
                        double_index = (double_index + gap) % self.table_size
                    if double_index == hash_value:
                        return

    def find(self, key):
        pass

    def get_slot(self, key):
        return self.primary_Hash_Function(key, self.params[0], self.table_size)

    def get_load(self):
        return self.total_elements / self.table_size
        pass

    def __str__(self):
        pass

    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass

class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        pass

    def insert(self, key):
        super().insert(key)
        pass

    def find(self, key):
        hash_value = self.primary_Hash_Function(key, self.params[0], self.table_size)
        if self.collision_type == "Chain":
            current_chain = self.hash_table[hash_value]
            if current_chain == -1:
                return False
            else:
                for entry in current_chain:
                    if entry == key:
                        return True
                return False

        elif self.collision_type == "Linear":
            linear_index = hash_value
            while True:
                if self.hash_table[linear_index] == -1:
                    return False
                elif self.hash_table[linear_index] == key:
                    return True
                else:
                    linear_index = (linear_index + 1) % self.table_size
                if linear_index == hash_value:
                    return False
        else:
            double_index = hash_value
            gap = self.secondary_Hash_Function(key, self.params[1], self.params[2])
            while True:
                if self.hash_table[double_index] == -1:
                    return False
                elif self.hash_table[double_index] == key:
                    return True
                else:
                    double_index = (double_index + gap) % self.table_size
                if double_index == hash_value:
                    return False

    def get_slot(self, key):
        return super().get_slot(key)

    def get_load(self):
        return super().get_load()

    def __str__(self):
        ans = ""
        if self.collision_type == "Chain":
            for i, slot in enumerate(self.hash_table):
                if slot == -1:
                    ans += "<EMPTY>"
                else:
                    ans += " ; ".join(str(item) for item in slot)
                if i != self.table_size - 1:
                    ans += " | "
        else:
            for i, slot in enumerate(self.hash_table):
                if slot == -1:
                    ans += "<EMPTY>"
                else:
                    ans += str(slot)
                if i != self.table_size - 1:
                    ans += " | "
        return ans

    def items(self):
        keys = []
        for slot in self.hash_table:
            if slot != -1:
                if self.collision_type == "Chain":
                    keys.extend(slot)
                else:
                    keys.append(slot)
        return keys


class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        pass

    def insert(self, x):
        super().insert(x)
        # pass

    def find(self, key):
        hash_value = self.primary_Hash_Function(key, self.params[0], self.table_size)
        if self.collision_type == "Chain":
            current_chain = self.hash_table[hash_value]
            if current_chain == -1:
                return None
            else:
                for entry in current_chain:
                    if entry[0] == key:
                        return entry[1]
                return None

        elif self.collision_type == "Linear":
            linear_index = hash_value
            while True:
                if self.hash_table[linear_index] == -1:
                    return None
                elif self.hash_table[linear_index][0] == key:
                    return self.hash_table[linear_index][1]
                else:
                    linear_index = (linear_index + 1) % self.table_size
                if linear_index == hash_value:
                    return None
        else:
            double_index = hash_value
            gap = self.secondary_Hash_Function(key, self.params[1], self.params[2])
            while True:
                if self.hash_table[double_index] == -1:
                    return None
                elif self.hash_table[double_index][0] == key:
                    return self.hash_table[double_index][1]
                else:
                    double_index = (double_index + gap) % self.table_size
                if double_index == hash_value:
                    return None

    def get_slot(self, key):
        return super().get_slot(key)

    def get_load(self):
        return super().get_load()

    def __str__(self):
        ans = ""
        if self.collision_type == "Chain":
            for i, slot in enumerate(self.hash_table):
                if slot == -1:
                    ans += "<EMPTY>"
                else:
                    ans += " ; ".join(f"({item[0]},{item[1]})" for item in slot)
                if i != self.table_size - 1:
                    ans += " | "
        else:
            for i, slot in enumerate(self.hash_table):
                if slot == -1:
                    ans += "<EMPTY>"
                else:
                    ans += f"({slot[0]},{slot[1]})"
                if i != self.table_size - 1:
                    ans += " | "
        return ans
