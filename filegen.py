#!/usr/bin/env python
#
# generate a large number of files for archiving in TSM
#
import string
from itertools import cycle

# generate 10GB files
size = 10**10
# generate 10MB files
# size = 10**7
# outdir = "/home/storteam/buffer"
# outdir = "/home/storteam/tstfiles"
outdir = "/media/T00017"
flcnt = 100

def gen(top):
    r = 0
    while r < top:
        r += 1
        yield r
        
pool = cycle(string.ascii_lowercase + string.digits)

for flnbr in range(0,flcnt):
    fl = "FILE{:0>10d}.dat".format(flnbr)
    with open(outdir + "/" + fl,"wt") as f:
        for i in gen(size):
            f.write(pool.next())
