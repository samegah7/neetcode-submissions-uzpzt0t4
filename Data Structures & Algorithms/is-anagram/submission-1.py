class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str1 = Counter(s.lower())
        str2 = Counter(t.lower())
        
        return str1 == str2
        