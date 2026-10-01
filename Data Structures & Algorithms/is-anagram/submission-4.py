class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams should be the same size
        # check the count of each letter
        # then compare the 2 dictionaries

        s_count = {}
        t_count = {}

        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] not in s_count:
                    s_count[s[i]] = 1
                else:
                    s_count[s[i]] += 1

            for i in range(len(t)):
                if t[i] not in t_count:
                    t_count[t[i]] = 1
                else:
                    t_count[t[i]] += 1

        else:
            return False

        if s_count == t_count:
            return True
        return False
                
         