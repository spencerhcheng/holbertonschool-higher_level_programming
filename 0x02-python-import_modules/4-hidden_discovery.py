#!/usr/bin/python3
if __name__ == "__main__":
    import sys, hidden_4
    names = dir(hidden_4)
    for dir in names:
        if dir[:2] != "__":
            print(dir)
