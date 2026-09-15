class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_s = {}
        temp_t = {}
        for x in s:
            if x not in temp_s:
                temp_s[x] = 1
            else:
                temp_s[x] += 1
        
        for x in t:
            if x not in temp_t:
                temp_t[x] = 1
            else:
                temp_t[x] += 1

        return temp_s == temp_t


        
