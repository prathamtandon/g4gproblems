import unittest
"""
Given M students and N books, where each book i has pages[i] number of pages, we need to assign
books to students such that each book is assigned to only one student and each student gets
at least one book. Also, we must minimize the maximum number of pages allocated to a student.
Input: P = [12, 34, 67, 90], M = 2
Output: 113
Explanation:
[12] and [34, 67, 90] Maximum pages = 191
[12, 34] and [67, 90] Maximum pages = 157
[12, 34, 67] and [90] Maximum pages = 113
Hence, minimum of maximum pages = 113
"""

"""
Approach:
1. The idea is to do a binary search for maximum pages per student.
2. For each maximum page value, we see how many students will be required to create valid assignment
   with that value.
3. If number of students exceeds maximum number of students, we try with a larger value of maximum pages per student.
4. If assignment is possible, we try with a smaller value of maximum pages per student.
NOTE: This is part of general strategy of problem solving called SIMULATION or OPTIMAL PAIR MATCHING.
"""


def page_allocation(pages, M):
    N = len(pages)
    result = float('inf')
    if N < M:
        return -1
    total_pages = sum(pages)
    start = min(pages)
    end = total_pages

    while start <= end:
        mid = (start + end) / 2
        if assignment_possible(pages, M, mid):
            result = min(result, int(mid))
            end = mid - 1
        else:
            start = mid + 1

    return result


def assignment_possible(pages, num_students, max_allowed_pages):
    students_required = 1
    current_pages = 0

    for i in range(len(pages)):
        if pages[i] > max_allowed_pages:
            return False
        if current_pages + pages[i] > max_allowed_pages:
            current_pages = pages[i]
            students_required += 1
            if students_required > num_students:
                return False
        else:
            current_pages += pages[i]

    return True


class TestPageAllocation(unittest.TestCase):

    def test_page_allocation(self):
        pages = [12, 34, 67, 90]
        M = 2
        self.assertEqual(page_allocation(pages, M), 113)
