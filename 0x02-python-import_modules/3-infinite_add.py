#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = sys.argv[1:]
    result = sum(int(i) for i in n)
    print("{}".format(result))
