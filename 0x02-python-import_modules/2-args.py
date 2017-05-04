#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    cmdLength = len(sys.argv)
    if cmdLength == 1:
        print('{:d} argument.'.format(cmdLength - 1))
    elif cmdLength == 2:
        print((cmdLength - 1), 'argument:')
        print(cmdLength - 1, ':', str(sys.argv[1]))
    elif cmdLength > 2:
        print('{:d} arguments:'.format(cmdLength - 1))
        for i in range(1, cmdLength):
            print(i, ":", str(sys.argv[i]))
