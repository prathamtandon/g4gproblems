import unittest
"""
Given n non negative integers representing an elevation map where width of each bar is 1,
compute how much water it is able to trap after raining.
Input: 2 0 2
Output: 2
Input: 3 0 0 2 0 4
Output: 10
"""

"""
Approach:
1. A bar can store water if there are taller bars to its left and right.
2. We can find the amount of water stored at each bar by finding the tallest bars to its left and right.
3. We then scan the bars from left to right and add the amount of water as min(left,right)-height(bar).
"""


def trapping_rain_water(list_of_bars):

    tallest_to_left = [0] * len(list_of_bars)
    tallest_to_right = [0] * len(list_of_bars)

    tallest_to_left[0] = list_of_bars[0]
    for i in range(1, len(list_of_bars)):
        tallest_to_left[i] = max(list_of_bars[i], tallest_to_left[i-1])

    tallest_to_right[len(list_of_bars)-1] = list_of_bars[len(list_of_bars)-1]
    for i in range(len(list_of_bars)-2, -1, -1):
        tallest_to_right[i] = max(list_of_bars[i], tallest_to_right[i + 1])

    water = 0

    for i in range(len(list_of_bars)):
        water += min(tallest_to_left[i], tallest_to_right[i]) - list_of_bars[i]

    return water


class TestTrappingRainWater(unittest.TestCase):

    def test_trapping_rain_water(self):
        list_of_bars = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(trapping_rain_water(list_of_bars), 6)
