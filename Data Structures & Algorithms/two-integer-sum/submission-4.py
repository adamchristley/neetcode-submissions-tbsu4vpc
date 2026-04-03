class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap Approach
        
        seen = {}

        for i, num in enumerate(nums): #for the index in enumerate(nums) looping nums 
                                       # essentially with i set as the index
            diff = target - num  # setting the state for diff
            if diff in seen: # If target is found
                return [seen[diff], i] # Print the output of the value in hashmap and 
                                       #the current index that equal the target.
            seen[num] = i # Updating the seen values into the hashmap from the current index