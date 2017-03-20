"""
Given a list of words, and a limit on number of characters that can be put
in one line (line width), put line breaks in given sequence such that lines are
printed neatly.
"""

"""
This little piece of code below is as good as it can get !!
It creates a memoized version of any function using function closures.
Sample usage:
Non-memoized function call:
>>f(a,b)
Memoized function call:
>>f_memo = memoize(f)
>>f_memo(a,b)
"""


def memoize(f):

    def memf(*args):
        if args not in memf.cache:
            memf.cache[args] = f(*args)
        return memf.cache[args]

    memf.cache = {}
    return memf


def word_wrap(word_list, start_col, max_width):
    if len(word_list) == 0:
        return '', 0

    first_word = word_list[0]
    rest_words = word_list[1:]
    end_col = start_col + len(first_word)

    # word doesn't fit on a line, return 'infinite' cost
    if end_col > max_width:
        return '', 1e9

    # Case 1: Line break after first word
    # Rest of the words placed starting on a newline.
    r1, c1 = word_wrap(rest_words, 0, max_width)
    r1 = first_word + '\n' + r1
    c1 += (max_width - end_col) ** 3  # compute end of line penalty

    # Case 2: No line break after first word
    # Rest of the words placed after current word including the single separating space.
    r2, c2 = word_wrap(rest_words, end_col + 1, max_width)
    r2 = first_word + ' ' + r2

    return (r1, c1) if c1 < c2 else (r2, c2)


if __name__ == '__main__':
    wlist = tuple('Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium '
                  'doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore '
                  'veritatis et quasi architecto beatae vitae dicta sunt explicabo. '
                  'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, '
                  'sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. '
                  'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, '
                  'adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et '
                  'dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, '
                  'quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi '
                  'ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit '
                  'qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui '
                  'dolorem eum fugiat quo voluptas nulla pariatur'.split(' '))

    word_wrap = memoize(word_wrap)
    print word_wrap(wlist, 0, 40)[0]



