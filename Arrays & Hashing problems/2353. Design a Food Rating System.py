
#https://leetcode.com/problems/design-a-food-rating-system/editorial/
from sortedcontainers import SortedSet
from collections import defaultdict
class FoodRatings:
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineToFoods = defaultdict(SortedSet)
        self.foodToCuisine = {}
        self.foodToRating = {}
        for i in range(len(foods)):
            self.cuisineToFoods[cuisines[i]].add((-ratings[i],foods[i]))
            self.foodToCuisine[foods[i]] = cuisines[i]
            self.foodToRating[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisine[food]
        self.cuisineToFoods[cuisine].remove((-self.foodToRating[food],food))
        self.cuisineToFoods[cuisine].add((-newRating,food))
        self.foodToRating[food] = newRating

        

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineToFoods[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)