#!/usr/bin/env python
import csv
from collections import defaultdict
from itertools import groupby
from operator import itemgetter

def grouped_by_category():
    groups = defaultdict(list)
    with open("UnicodeData.txt") as f:
        r = csv.reader(f, delimiter=';')
        for row in r:
            groups[row[2]].append(int(row[0], 16))
    return groups

def match_category(category):
    return category.startswith('L') and category != 'Lo'

letters = sorted((code for category, codes in grouped_by_category().items() if match_category(category) for code in codes if code <=0xffff))

def last_first(g):
    return format_range(g[0], g[-1])

def format_codepoint(c):
    return '\\u%04x' % c

def format_range(f, t):
    return '%s-%s' % (format_codepoint(f), format_codepoint(t))

print ''.join((last_first(map(itemgetter(1), g)) for k, g in groupby(enumerate(letters), lambda (i,x):i-x)))
