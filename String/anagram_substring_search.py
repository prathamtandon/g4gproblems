"""
Given a text txt[0...n-1] and pattern pat[0...m-1], write a function to search all occurrences
of pattern and its permutations (or anagrams) in text. Expected time complexity is O(n).
Input:
txt: "ABAABA"
pat: "BA"

Output: 2 occurrences at indices: 0, 4
"""


"""
Approach:
1. The idea is to use a sliding window in text string.
2. Maintain two arrays to count the number of characters in pattern and current window of text.
3. If the count values are same, its a match. (For permutation, we are only concerned with counts).
4. To slide the window by one position, we just decrement count of leftmost character by 1, and increment
   count of next character by 1. (Idea similar to Rabin-Karp pattern search rolling hash function).
NOTE: Assuming we are dealing with same character set of txt and pattern of size 256.
"""

CHARSET_SIZE = 256


def compare(arr1, arr2):
    for i in range(CHARSET_SIZE):
        if arr1[i] != arr2[i]:
            return False

    return True


def search_anagrams(txt, pat):
    m = len(pat)

    countP = [0] * CHARSET_SIZE
    countT = [0] * CHARSET_SIZE

    for i in range(m):
        countP[ord(pat[i])] += 1
        countT[ord(txt[i])] += 1

    for i in range(m, len(txt)):

        if compare(countP, countT):
            print "Found at index ", i - m

        countT[ord(txt[i])] += 1
        countT[ord(txt[i - m])] -= 1

    if compare(countP, countT):
        print "Found at index ", len(txt) - m


if __name__ == '__main__':
    txt = 'BACDGABCDA'
    pat = 'ABCD'
    search_anagrams(txt, pat)
