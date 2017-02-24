"""
Given N men and N women, where each person has ranked all members of the opposite sex
in order of preference, marry the man and woman in such a way that there are no two people
of opposite sex who would both rather have each other than their current assigned partners.
Input: m1: w1,w2
       m2: w1,w2
       w1: m1,m2
       w2: m1,m2
A stable marriage would be (m1,w1) and (m2,w2). However, (m1,w2) and (m2,w1) is not stable marriage
as m1 and w1 would both rather be with each other than their current partners (as per their preference lists).
"""


"""
Approach (only):
1. The idea is to assign partners to free men while there are still free men.
2. For each free man, go through each woman in order of his preference list.
3. If a woman has not been assigned yet, assign her and mark the man as assigned.
4. Otherwise, if a woman has already been assigned, check if she would prefer this man over her current
   assigned man (based on her preference list). If so, then break the current assignment and make a new
   assignment. Also mark the current assigned man as free.
"""
