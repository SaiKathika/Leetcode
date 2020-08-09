#Here I did this problem in three ways
#more efficient (using vector 100ms)
#https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/683361/C%2B%2B-Java-Python3-Real-O(1)-100-Java-98-c%2B%2B-Explained-in-Detail.
#https://www.youtube.com/watch?v=hT43xpai5s0&feature=youtu.be (watch from 2:05 till 8:45)
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._nums = []
        self._positions = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._positions:
            return False
        self._nums.append(val)
        self._positions[val] = len(self._nums)-1
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self._positions:
            return False
        
        pos = self._positions[val]
        self._nums[pos] = self._nums[-1]
        self._positions[self._nums[pos]] = pos
        self._nums.pop()
        self._positions.pop(val)
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self._nums[random.randint(0, len(self._nums)-1)]
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

#using dictionary (not efficient 388ms)
import random

class RandomizedSet:

    def __init__(self):
        self.data = {}
        
    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data[val] = val
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if val in self.data:
            del self.data[val]
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(list(self.data))

#Using Set (not efficient (450ms))
import random

class RandomizedSet:

    def __init__(self):
        self.data = set()
        
    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.data))
