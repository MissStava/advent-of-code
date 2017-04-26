import re

# file = open("../inputs/day4.txt", "r")

# for line in file:

string = "bnmrtldq-fqzcd-bqxnfdmhb-bgnbnkzsd-zmzkxrhr-105[bdnzm]"

print re.search('\[([a-z]{5})\]', string).group(1)