class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict1 = {}
        for i in s:
            if i in my_dict1.keys():
                my_dict1[i] += 1
            else: 
                my_dict1[i] = 1

        my_dict2 = {}
        for i in t:
            if i in my_dict2.keys():
                my_dict2[i] += 1
            else: 
                my_dict2[i] = 1

        if my_dict1 == my_dict2:
            return True
        else: 
            return False
        
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))