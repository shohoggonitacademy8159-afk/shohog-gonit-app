import sys, re
# ব্যবহার: python3 addq.py file.txt  (stdin: '1.2<TAB>লাইন')
f = sys.argv[1]; lines = open(f, encoding='utf-8').read().split('\n')
for row in sys.stdin.read().strip().split('\n'):
    sec, q = row.split('\t', 1)
    i = lines.index('## ' + sec); j = i + 1
    while j < len(lines) and not lines[j].startswith('## '): j += 1
    while lines[j - 1].strip() == '': j -= 1
    lines.insert(j, q)
open(f, 'w', encoding='utf-8').write('\n'.join(lines))
