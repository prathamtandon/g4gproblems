"""
Given an array of length n, return the majority element - An element that occurs more than n/2 times.
Input : 3 3 4 2 4 4 2 4 4
Output : 4
Input : 3 3 4 2 4 4 2 4
Output : None
"""
import unittest

"""
Approach 1:
1. Initialize a dictionary
2. If item not present, insert it with count = 1
3. If item already present, increment count by 1
4. If count > n/2 return item
"""

"""
Approach 2:
Moore's voting algorithm:
1. FindCandidate:
    1.1 Initialize majority element as first element, set its count = 1
    1.2 For each element equal to majority element, increment count by 1, else decrement count by 1
    1.3 If count becomes zero, reinitialize majority element
    NOTE: For an element to be majority, it MUST occur consecutively in the array at least once!.
    This runs in linear time.
2. CheckMajority
    2.1 Find the actual count of majority element and see if its > n/2
"""


def moore_voting_find_candidate(list_of_numbers):
    majority_index = 0
    count = 1

    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i] == list_of_numbers[majority_index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority_index = i
            count = 1

    return list_of_numbers[majority_index]


def moore_voting_check_majority(list_of_numbers, candidate):
    count = 0
    threshold = len(list_of_numbers) / 2

    for num in list_of_numbers:
        if num == candidate:
            count += 1
            if count > threshold:
                return True

    return False


def moore_voting_majority_element(list_of_numbers):
    candidate = moore_voting_find_candidate(list_of_numbers)
    if moore_voting_check_majority(list_of_numbers, candidate):
        return candidate
    else:
        return None


class TestMajorityElement(unittest.TestCase):

    def test_moore_voting_majority_preset(self):
        list_of_numbers = [3, 3, 4, 2, 4, 4, 2, 4, 4]
        candidate = moore_voting_majority_element(list_of_numbers)
        self.assertEqual(candidate, 4)

    def test_moore_voting_majority_absent(self):
        list_of_numbers = [3, 3, 4, 2, 4, 4, 2, 4]
        candidate = moore_voting_majority_element(list_of_numbers)
        self.assertIsNone(candidate)


if __name__ == '__main__':
    unittest.main()
