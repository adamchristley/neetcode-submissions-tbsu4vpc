class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # Setting up the groups dictionary for sorting 

        for s in strs: # Iterating through all of the strings one by one
            key = "".join(sorted(s)) # This creates the keys to organize each anagram independantly to add each to the sorted dict
            groups[key].append(s) # This line will add the keys to the groups dict by individual key value via append s
        return list(groups.values()) # return the list content by each anagram found in the strs, sorted in groups