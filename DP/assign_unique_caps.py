import unittest
"""
Given n people, each person having a collection of caps, where each cap has a unique id between 1 and 100,
find the number of ways to assign caps to people such that no two persons wear the same cap. ie all unique
assignments.
Input: n = 3
cap_list[0] = [5, 100, 1]
cap_list[1] = [2]
cap_list[2] = [5, 100]
Output: 4   (5, 2, 100), (100, 2, 5),
            (1, 2, 5) and  (1, 2, 100)
Since, number of ways could be large, so output modulo 1000000007
"""


"""
Approach:
Optimal substructure: caps(current_assignment, cap_i) = caps(current_assignment, cap_i+1) ie don't include cap_i +
    caps(new_assignment, cap_i+1) where new_assignment is every possible assignment of cap_i to possible persons.

We use a bitmask to track assignments.
For example, if there are 4 persons (0,1,2,3), then 1001 means person 0 and person 3 are wearing caps.
caps(1111, 100) stores the final result (ie all persons are assigned a cap). We solve this using
top-down with memoization.
"""

MOD = 1000000007
NUM_CAPS = 100


def cap_assignment(mask, num_persons, cap_id, table, cap_list):

    if mask == ((1 << num_persons) - 1):
        return 1
    if cap_id > NUM_CAPS:
        return 0
    if table[mask][cap_id] != -1:
        return table[mask][cap_id]

    # excluding current cap_id
    ways = cap_assignment(mask, num_persons, cap_id + 1, table, cap_list)
    for j in cap_list[cap_id]:
        if mask & (1 << j):
            continue
        # including current cap_id with assignments to all possible persons who own it.
        ways += cap_assignment(mask | (1 << j), num_persons, cap_id + 1, table, cap_list)
        ways %= MOD

    table[mask][cap_id] = ways
    return ways


class TestCapAssignments(unittest.TestCase):

    def test_cap_assignments(self):
        n = 3
        table = [[-1] * (NUM_CAPS+1) for _ in range(1 << n)]
        cap_list = [[] for _ in range(NUM_CAPS+1)]
        # cap_list[j] is list of all persons (0 indexed) who possess cap j for j = 1,...,100
        cap_list[1] = [0]
        cap_list[2] = [1]
        cap_list[5] = [0, 2]
        cap_list[100] = [0, 2]

        self.assertEqual(cap_assignment(0, n, 1, table, cap_list), 4)

