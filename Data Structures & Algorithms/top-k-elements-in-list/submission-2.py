class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {};
        result = [];

        
        for num in nums: # Iterates through each number in array "list"
            if num in count:
                count[num] += 1 # If number is in count/has been seen then +1
            else: 
                count[num] = 1 # If number isn't in count/hasn't been seen then set it to 1 
        solution = sorted(count.items(), key=lambda x: x[1], reverse = True)
        # Sorting. list numbers and freq, use lambda x[1] to count freq. and use reverse to go 
        # from highest to lowest


        for i in range(k): # Iterates for k length using i index and range(k)
            result.append(solution[i][0])  # add the number and freq and [0] gets the number

        return result
