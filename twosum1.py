from typing import List
import time

# Approach 1 using inefficient brute force
nums = [2,7,11,15]
target = int(9)

class BruteForceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bool = [0] * len(nums) #copy array to track which index has been iterated on
        for i in range(len(nums)):
            while bool[i] == 0:
                for j in range(len(nums)):
                    if ((nums[i] + nums[j]) == target) and (i != j):
                        return[i,j]
                bool[i] = 1

t = time.time() # time it

myBruteSol = BruteForceSolution()
myBruteSol.twoSum(nums, target)

elapsed = time.time() - t
print(elapsed)

# Time complexity: o(n^2)
# Space complexity: o(1) since constant input size

# Approach 2 using Two Pass Hash Table

class HashTableSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i # creates a hashmap
        for i in range(len(nums)):
            complement = target - nums[i] # takes an element and substracts the target
            if complement in hashmap and hashmap[complement] != i: # looks for the remainder in the element and returns the index
                return [i, hashmap[complement]]

t = time.time()
myHashSol = HashTableSolution()
myHashSol.twoSum(nums, target)
elapsed = time.time() - t
print(elapsed)

# Time complexity: o(n)
# Space complexity: o(n) hashmap requires extra space of n elements

# Approach 3 using One Pass Hash Table
# One loop can be used instead of two, checks happen whilst hashmap is populates

class OnePassHashTableSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap: # if it already exists then return
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i #populate hash map


t = time.time()
myOnePassSol = OnePassHashTableSolution()
myOnePassSol.twoSum(nums, target)
elapsed = time.time() - t
print(elapsed)

# Time complexity: o(n)
# Space complexity: o(n) hashmap requires extra space of n elements