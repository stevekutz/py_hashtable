class HashItem:
     def __init__(self, key, value):
          self.key  
          self.value

class HashTable:
     def __init__(self):
          self.size = 256
          self.slots = [None for i in range(self.size)]          
          self.count = 0


