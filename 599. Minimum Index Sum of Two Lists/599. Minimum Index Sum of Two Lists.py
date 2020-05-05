"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hmap,result,least_sum = {},[],sys.maxsize
        for i,restaurant in enumerate(list1):
            hmap[restaurant] = i
        for i,restaurant in enumerate(list2):
            if restaurant in hmap.keys():
                print(i + hmap.get(restaurant))
                if i + hmap.get(restaurant) < least_sum:
                    least_sum = i + hmap.get(restaurant)
                    result = [restaurant]
                elif i + hmap.get(restaurant) == least_sum:
                    result.append(restaurant)
        return result