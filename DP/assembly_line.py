import unittest


def assembly_line(time_spent_at_station, time_spent_on_switch, entry, exit):
    # table1[i] denotes time taken to leave station i for line 1
    # table2[i] denotes time taken to leave station i for line 2
    n = len(time_spent_at_station[0])
    table1 = [0] * (n+1)
    table2 = [0] * (n+1)
    table1[1] = entry[0] + time_spent_at_station[0][0]
    table2[1] = entry[1] + time_spent_at_station[1][0]

    for i in range(2, n+1):
        table1[i] = min(table1[i-1] + time_spent_at_station[0][i-1],
                        table2[i-1] + time_spent_on_switch[1][i-1] + time_spent_at_station[0][i-1])
        table2[i] = min(table2[i-1] + time_spent_at_station[1][i-1],
                        table1[i-1] + time_spent_on_switch[0][i-1] + time_spent_at_station[1][i-1])

    return min(table1[n] + exit[0], table2[n] + exit[1])


class TestAssemblyLine(unittest.TestCase):

    def test_assembly_line(self):
        time_spent_at_station = [[4, 5, 3, 2], [2, 10, 1, 4]]
        time_spent_on_switch = [[0, 7, 4, 5], [0, 9, 2, 8]]
        entry = [10, 12]
        exit = [18, 7]
        self.assertEqual(assembly_line(time_spent_at_station, time_spent_on_switch, entry, exit), 35)

