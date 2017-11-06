"""Find longest sequence of zeroes in binary representation of an Integer"""

from helpers import print_out


@print_out
def solution(N):
    br = str(bin(N))[2:]
    print 'binary repr:', br
    br = br.strip('0')
    seqs = br.split('1')
    return max((len(x) for x in seqs))


test_input = [5, 6, 51712, 20, 1041]

for item in test_input:
    solution(item)
