
class Solution:
    def __init__(self) -> None:
        self.dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        self.subs_dict = {
            'I' : -1,
            'X' : -10,
            'C' : -100,
        }
        self.dict_list = [key for key in self.dict.keys()]

    def prevChecker(self, prev:str, curr:str) -> bool:
        return self.dict_list.index(prev) < self.dict_list.index(curr)

    def romanToInt(self, s: str) -> int:
        number = 0
        for i in range(len(s)):
            if i == 0:
                continue
            if s[i-1] in self.subs_dict.keys():
                if self.prevChecker(s[i-1], s[i]):
                    number += self.subs_dict[s[i-1]]
                else:
                    number += self.dict[s[i-1]]
            else:
                number += self.dict[s[i-1]]
        else:
            number += self.dict[s[i]]
        return number

s = Solution()
print(s.romanToInt('MCMXCIV'))