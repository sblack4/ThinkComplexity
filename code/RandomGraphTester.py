from RandomGraph import * 


def main(script, n=26, p=0.01, pIncrement=.01, pEnd=.5, num=100, *args):
    n = int(n)
    p = float(p)
    num = int(num)
    while(p<float(pEnd)):
        count = test_p(n, p, num)
        print '== nodes: %s, probabilty: %s, #connected: %s, iterations: %s ==' % (str(n), p, count, num)
        p += pIncrement
        while(n<100):
            count = test_p(n, p, num)
            print '== nodes: %s, probabilty: %s, #connected: %s, iterations: %s ==' % (str(n), p, count, num)
            n += 5
        n=26

if __name__ == '__main__':
    import sys
    main(*sys.argv)