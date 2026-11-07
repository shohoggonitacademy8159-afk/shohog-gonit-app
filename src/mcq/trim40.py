#!/usr/bin/env python3
"""প্রতি পাঠে 40-এর বেশি প্রশ্ন থাকলে শেষের দিক থেকে অতিরিক্ত (মধ্যম আগে) বাদ দেয়; কম থাকলে কত কম তা দেখায়।"""
import sys, collections
f = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 40
lines = open(f, encoding='utf-8').read().splitlines()
secs = collections.OrderedDict(); cur = None; head = []
for l in lines:
    if l.startswith('## '): cur = l; secs[cur] = []
    elif l.strip() and cur: secs[cur].append(l)
out = []; short = {}
for s, q in secs.items():
    q = list(dict.fromkeys(q))
    while len(q) > N:
        idx = max((i for i, x in enumerate(q) if x.startswith('m|')), default=len(q) - 1)
        q.pop(idx)
    if len(q) < N: short[s[3:]] = N - len(q)
    out += [s] + q
open(f, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('short:', short)
