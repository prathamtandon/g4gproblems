import unittest
"""
Given two strings str1 and str2, find the minimum cost of operations:
1. Insert
2. Remove
3. Replace
to convert str1 to str2. Operations are only performed on str1.
Input:
str1 = 'sunday'
str2 = 'saturday'
Output:
3
"""

"""
Approach:
1. If str1[i] == str2[j] then return edit_distance(str1,str2,i-1,j-1)
2. Else, return minimum among:
    (a) Insert (str1,str2,i,j-1)
    (b) Remove (str1,str2,i-1,j)
    (c) Replace (str1,str2,i-1,j-1)
3. If len(str1) == 0: return len(str2) ie we need to do len(str2) inserts.
4. If len(str2) == 0: return len(str1) ie we need to do len(str1) removes.
"""


def edit_distance(first_str, second_str):

    m = len(first_str)
    n = len(second_str)

    table = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif first_str[i-1] == second_str[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])

    return table[m][n]


class TestEditDistance(unittest.TestCase):

    def test_edit_distance(self):
        first_string = 'sunday'
        second_string = 'saturday'
        self.assertEqual(edit_distance(first_string, second_string), 3)
