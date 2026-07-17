from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 26 characters from a to z in order
        #alphabet = [0] * 26

        #if two words are anagram to each other 
        #than the alphabet are the exactly the same. 
        #so we can choose the alphabet as the key in our hashmap, and the value would be the word itself

        res = []
        Map = defaultdict(list)

        #iteration and recording
        for word in strs:
            alphabet = [0] * 26
            for cha in word:
                alphabet[ord(cha) - ord('a')] += 1
        
            #dump it into our hashmap, and since list is mutable(unhashble), so we change into the tuple
            Map[tuple(alphabet)].append(word)
        
        for key, value in Map.items():
            res.append(value)
        
        return res