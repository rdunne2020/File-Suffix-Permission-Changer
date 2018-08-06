#!/usr/bin/env python3
from os import listdir, rename, chmod

files = listdir(".")
good_suff = ".trc.txt"
bad_suff = ".vid.bin.trc.txt"


for parts in files:
    if parts.endswith(bad_suff):
        chmod(parts, 0o644)
        rename(parts, parts[:len(parts)-len(bad_suff)] + good_suff)
        print("Renamed and chmodded")
        
