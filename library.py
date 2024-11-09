import hash_table as ht
class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE

    def mergeSort2(self, arr, start, end):
        if start >= end:
            return [arr[start]]  
            
        mid = (start + end) // 2
        left_sorted = self.mergeSort2(arr, start, mid)
        right_sorted = self.mergeSort2(arr, mid + 1, end)
        
        return self.merge2(left_sorted, right_sorted)

    def merge2(self, left, right):
        temp = []
        left_idx, right_idx = 0, 0

       
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx][0] < right[right_idx][0]:  
                temp.append(left[left_idx])
                left_idx += 1
            else:
                temp.append(right[right_idx])
                right_idx += 1

        # Append remaining elements of the left partition
        while left_idx < len(left):
            temp.append(left[left_idx])
            left_idx += 1

        # Append remaining elements of the right partition
        while right_idx < len(right):
            temp.append(right[right_idx])
            right_idx += 1

        return temp

    def mergeSort(self, arr, start, end):
        if start >= end:
            return [arr[start]]  

        mid = (start + end) // 2
        left_sorted = self.mergeSort(arr, start, mid)
        right_sorted = self.mergeSort(arr, mid + 1, end)
        
        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        temp = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                temp.append(left[left_idx])
                left_idx += 1
            else:
                temp.append(right[right_idx])
                right_idx += 1

        while left_idx < len(left):
            temp.append(left[left_idx])
            left_idx += 1

        while right_idx < len(right):
            temp.append(right[right_idx])
            right_idx += 1

        return temp


    def remove_duplicates(self, arr):
        if not arr:
            return []  
        result = [arr[0]] 
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                result.append(arr[i])
        return result


    def unique_sort(self, arr):
        ans=self.mergeSort(arr, 0, len(arr)-1)
        return self.remove_duplicates(ans)

    def __init__(self, book_titles, texts):
        self.book_table=[]
        for ind in range(len(book_titles)):
            self.add_book(book_titles[ind] , texts[ind])

        self.book_table = self.mergeSort2(self.book_table, 0, len(self.book_table) - 1)

        pass



    def add_book(self, book_title, text):
        # leter=[]
        # for x in text:
        #     leter.append(x)
        leter=self.unique_sort(text)
        self.book_table.append((book_title, leter))

    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid][0] == target:
                return mid  
            elif arr[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1  

    def binary_search2(self, arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid  # Target found, return its index
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1  # Target not found

    def distinct_words(self, book_title):
        index=self.binary_search(self.book_table, book_title)
        return self.book_table[index][1]
        
    
    def count_distinct_words(self, book_title):
        index=self.binary_search(self.book_table, book_title)
        return len(self.book_table[index][1])
    
    
    def search_keyword(self, keyword):
        ans=[]
        for x in self.book_table:
            index=self.binary_search2(x[1], keyword)
            if index!=-1:
                ans.append(x[0])
        return ans

    
    def print_books(self):
        # for book in self.book_table:
        #     print(str(book[0]),":", end="")
        #     for x in book[1]:
        #         print(str(x), end="")
        #         if x!=book[1][-1]:
        #             print("|", end="")
        #     print()
        # print("Hello World")
        for book in self.book_table:
            print(f"{book[0]}: ", end="")
            print(" | ".join(book[1]))


class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.para=params
        self.collision=-1
        if name=="Jobs":
            self.collision="Chain"
        elif name=="Gates":
            self.collision="Linear"
        else:
            self.collision="Double"
        # self.letter_table=ht.HashSet(self.collision, params)
        self.book_table=ht.HashMap(self.collision, params)
        pass
    
    def add_book(self, book_title, text):
        word_table=ht.HashSet(self.collision , self.para)
        for x in text:
            word_table.insert(x)
        self.book_table.insert((book_title, word_table))


        pass
    
    def distinct_words(self, book_title):
        val=self.book_table.find(book_title)
        if val is None:
            return []
        return val.items()
    
    def count_distinct_words(self, book_title):
        val=self.book_table.find(book_title)
        if val is None:
            return 0
        else :
            return val.total_elements
        
    
    def search_keyword(self, keyword):
        ans = []
        for x in self.book_table.hash_table:
            if x != -1: 
                if self.collision == "Chain":
                    for item in x:  
                        if item[1].find(keyword):
                            ans.append(item[0])
                else:
                    if x[1].find(keyword):
                        ans.append(x[0])
        return ans

    
    def print_books(self):
        if self.collision == "Chain":
            for slot in self.book_table.hash_table:
                if slot!=-1:
                    for x in slot:
                        print(str(x[0]),end="")
                        print(": ", end="")
                        print(x[1].__str__())
                    # keys.extend(slot)

        else:
            for slot in self.book_table.hash_table:
                if slot != -1:
                    print(str(slot[0]), end="")
                    print(": ", end="")
                    print(slot[1].__str__())
                    # keys.append(slot)
        pass