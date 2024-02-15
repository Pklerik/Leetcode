from typing import List

class Solution:
    candy_list:list
    ratings:list
    reversed_candy_list:list
    
    def candy(self, ratings: List[int]) -> int:
        self.ratings = ratings
        candy_list = [1 for _ in range(len(ratings))]
        for i, _ in enumerate(ratings):
            if i == 0: continue
            if ratings[i] > ratings[i-1]:
                candy_list[i] = candy_list[i-1] + 1
            elif ratings[i] == ratings[i-1]:
                candy_list[i] = 1
        self.candy_list = candy_list
        
        reversed_ratings = ratings[::-1]
        reversed_candy_list = candy_list[::-1]
        
        for i, _ in enumerate(ratings[::-1]):
            if i == 0: continue
            if reversed_ratings[i] > reversed_ratings[i-1]:
                if reversed_candy_list[i] <= reversed_candy_list[i-1]:
                    reversed_candy_list[i] = reversed_candy_list[i-1] + 1
        self.reversed_candy_list = reversed_candy_list
        return sum(reversed_candy_list)
    
    def __str__(self) -> str:
        return f'Candy_list:{self.candy_list}, Ratings:{self.ratings}, New_candy_list:{self.reversed_candy_list[::-1]}'
    
print(Solution().candy([1,0,2]))