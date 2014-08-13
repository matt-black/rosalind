import sys, getopt

def main(argv):
    if len(argv) > 1:
        raise Exception('too many args!')
    else:
        val = fibonacci(int(argv[0]))
        print(val)

def fibonacci(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
    return a

if __name__ == "__main__":
    main(sys.argv[1:])
