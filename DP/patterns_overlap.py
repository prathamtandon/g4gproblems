import sys


def pattern_converter(pattern):
    ans = []

    for j in range(len(pattern)):
        if pattern[j] == '*':
            ans.append('*')
            ans.append('*')
            ans.append('*')
            ans.append('*')
        else:
            ans.append(pattern[j])

    return ''.join(ans)


def patterns_overlap_dp(pattern1, pattern2):
    pattern1 = pattern_converter(pattern1)
    pattern2 = pattern_converter(pattern2)
    m = len(pattern1)
    n = len(pattern2)
    table = [[False] * (n+1) for _ in range(m+1)]
    table[0][0] = True

    # This case is required when one pattern is empty and other contains only '*'.
    for i in range(1, m+1):
        if pattern1[i-1] == '*':
            table[i][0] = table[i-1][0]

    for i in range(1, n+1):
        if pattern2[i-1] == '*':
            table[0][i] = table[0][i-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if pattern1[i-1] == '*' and pattern2[j-1] == '*':
                table[i][j] = table[i-1][j] or table[i][j-1] or table[i-1][j-1]
            elif pattern1[i-1] == '*':
                table[i][j] = table[i-1][j] or table[i-1][j-1]
            elif pattern2[j-1] == '*':
                table[i][j] = table[i][j-1] or table[i-1][j-1]
            elif pattern1[i-1] == pattern2[j-1]:
                table[i][j] = table[i-1][j-1]

    return table[m][n]


def main():
    fin = open('B-large-practice.in')
    fout = open('output1.out', 'w')
    sys.stdout = fout
    num_tests = int(fin.readline().strip())
    case_counter = 1
    inputs = [fin.readline().strip() for i in range(num_tests*2)]
    for i in range(0, len(inputs)-1, 2):
        pattern1 = inputs[i]
        pattern2 = inputs[i+1]
        result = 'TRUE' if patterns_overlap_dp(pattern1, pattern2) else 'FALSE'
        print 'Case #' + str(case_counter) + ': ' + result
        case_counter += 1

    fout.close()

if __name__ == '__main__':
    main()
