class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list) # Instantiate the default dictionary 

        for s in strs: # for s (index) in strs (list of strings name), iterate
            key = "".join(sorted(s)) # setting key as the sorted s and joining specfically between ""
            # This is sorting the strings in strs and the next line appends each to a separte string
            # in the dictionary based on sorted "aet", "abc", etc.
            groups[key].append(s) # adding s to the array groups
        return list(groups.values()) # Returning the values of the groups dictionary by using values()

        