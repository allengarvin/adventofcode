#!/usr/bin/python3
# coding: utf-8

YEAR=2015

import os

languages = {
    "py" : ("python", "Python"),
    "c" : ("c", "C"),
    "rb" : ("ruby", "Ruby"),
    "rkt" : ("racket", "Racket"),
    "pike" : ("pike", "Pike"),
    "fs" : ("forth", "Forth"),
    "sh" : ("bash", "Bash"),
}

lang_keys = [
    "py",
    "rb",
    "c",
    "rkt",
    "pike",
    "fs",
    "sh",
]

line = "|    |"
for key in lang_keys:
    line += " %-12s |" % languages[key][1]
print(line)

line = "| -- |"
for key in lang_keys:
    line += " %-12s |" % ("-" * len(languages[key][1]))
print(line)

references = []

for i in range(1, 26):
    line = "| %2d |" % i
    for key in lang_keys:
        short, full = languages[key]

        if os.path.isfile("%02d/%02d-%s.%s" % (i, i, short, key)):
            line += " %3s%-9s |" % ('[✓]', '[%02d%s]' % (i, key))
            references.append("%-12s %s" % ('[%02d%s]:' % (i, key), 
                ("https://github.com/allengarvin/adventofcode/blob/main/%d/%02d/%02d-%s.%s" % (YEAR, i, i, short, key))))
        else:
            line += " %12s |" % ""
    print(line)

print()
print("\n".join(references))
    
