#!/usr/bin/python3
import sys

cmdLength = len(sys.argv)
if cmdLength == 1:
    print('{:d} argument.'.format(cmdLength - 1))
elif cmdLength == 2:
    print('{:d} argument:'.format(cmdLength - 1))

elif cmdLength > 2:
    print('{:d} arguments:'.format(cmdLength - 1))
    for i in range(1, cmdLength):
        print(i, ":", str(sys.argv[i]))
