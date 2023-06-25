import sys


# Constructing a table of partial matches to use in the KMP algorithm
def get_match_table(pat):
    pat_l = len(pat)

    if pat_l == 1:
        return [0] * pat_l
    else:
        hash_table = [0] * pat_l
        cur_pref_l = 0
        for i, c in enumerate(pat[1:], 1):

            while cur_pref_l > 0 and pat[cur_pref_l] != c:
                cur_pref_l = hash_table[cur_pref_l - 1]

            if pat[cur_pref_l] == c:
                cur_pref_l += 1
            hash_table[i] = cur_pref_l
        return hash_table


# The Knuth-Morris-Pratt algorithm
def kmp(text, pat):
    text_l ,pat_l= len(text),len(pat)

    start_index, cur_index, pat_i = 0, 0, 0
    matches = []
    hash_table = get_match_table(pat)

    while text_l - start_index > pat_l:

        while pat_i < pat_l and text[cur_index] == pat[pat_i]:
            cur_index += 1
            pat_i += 1

        if pat_i >= pat_l:
            matches.append(str(start_index))

        if pat_i > 0 and hash_table[pat_i - 1] > 0:
            start_index = cur_index - hash_table[pat_i - 1]
            pat_i = hash_table[pat_i - 1]

        else:
            if cur_index == start_index:
                cur_index += 1
            start_index = cur_index
            if pat_i > 0:
                pat_i = hash_table[pat_i - 1]

    if text[-pat_l:] == pat:
        matches.append(str(len(text) - pat_l))
    print(' '.join(matches))


flag = False
text_initial = ''
pat_initial = ''
for line in sys.stdin:
    if flag:
        text_initial = line.rstrip('\n')
        flag = False
        kmp(text_initial, pat_initial)

    else:
        pat_initial = line.rstrip('\n')
        flag = True


