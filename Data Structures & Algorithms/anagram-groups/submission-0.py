class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs: 
            frequency = [0] * 26
            for char in string:
                frequency[ord(char) - ord('a')] += 1
            key = tuple(frequency)
            if anagrams.get(key) == None: 
                anagrams[key] = [string]
            else:
                anagrams[key].append(string)
        return list(anagrams.values())