class HashItem:
     def __init__(self, key, value):
          self.key  
          self.value

class HashTable:
     def __init__(self):
          self.size = 256
          self.slots = [ [] for _ in range(self.size)]          
          self.count = 0

def _hash(self,key):
     mutl = 1
     hv = 0
     for ch in key:
          hv += mutl * ord(ch)
          mult += 1
     return hv % self.size     

def put(self, key, value):
     item = HashItem(key, value)
     h = self._hash(key)

def insert(hash_table, key, value):
     hash_key = hashing_func(key)


hash_table = [None] * 8   # 8 slots initialized to None

def my_hash(s):
     sb = s.encode()  # get UTF code for string

     total = 0

     for b in sb:
          total += b     
          total &= 0xffffffff  # lamp to 32 bits

     return total
def hash_index(key):
     h = my_hash(key)
     return h % len(hash_table)

def put(key, val):
     i = hash_index(key)     
     if hash_table[i] != None:
          print(f' Collision overwriting {repr(hash_table[i])}!')
     hash_table[i] = val

def get(key):
     i = hash_index(key)
     return hash_table[i]

def delete(key):
     i = hash_index(key)     
     hash_table[i] = None

put("Hello", "Hello Value")
put("World", "World Value")


print(hash_table)
print(get("Hello"))

class Node:
     def __init__(self, value):
          self.value = value
          self.next = None

class LinkedList:
     def __init__(self):
          self.head = None

     def find(self, value):
          cur = self.head

          while cur is not None:
               if cur.value == value:
                    return cur
               cur = cur.next

          return None

     def delete(self, value):
          cur = self.head

          if cur.value == value:
              self.head = cur.next
              return cur

          prev = cur
          cur = cur.next

          while cur is not None:
               if cur.value == value:
                    prev.next = cur.next   
                    return cur

               else:
                    prev = cur
                    cur = cur.next     
          
          return none

     def insert_at_head(self, node):
          none.next = self.head
          self.head = node
