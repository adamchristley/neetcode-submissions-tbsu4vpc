class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # Initializes the groups dict

        for s in strs: # loops through strs by key/index
            key = "".join(sorted(s)) # Joins string and sorts the string
            groups[key].append(s) # groups the strings together
        return list(groups.values()) # returns the groups of strings and their contents // value of group dict