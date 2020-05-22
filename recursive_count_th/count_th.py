'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # TBC
    if len(word) <= 2:
        if word == 'th':
            return 1
        else:
            return 0

    count = 0
    lastTwo = word[-2] + word[-1]

    if lastTwo == 'th':
        count = 1

    return count + count_th(word[:-1])


count_th('thasdfasdfthThthasdlthH')
print(count_th('thasdfasdfthThthasdlthH'))
