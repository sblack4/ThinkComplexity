"""
Ex 3-6
test LinearMap, BetterMap, and HashMap and charecterise their order of growth
"""


import matplotlib.pyplot as pyplot
from MapSoln import LinearMap, BetterMap, HashMap 
from listsum import etime, fit, plot, save 
from Exercise2_7 import infinite_alphanumeric_generator 


def testAddMap(mapObj, n):
    iter = infinite_alphanumeric_generator()

    start = etime()

    for i in range(0, n):
        mapObj.add(i, iter.next())
    end = etime()
    elapsed = end - start
    return elapsed


def testGetMap(mapObj, n):
    iter = infinite_alphanumeric_generator()

    start = etime()

    for i in range(0, n):
        getted = mapObj.get(i)
        assert(getted == iter.next())
    end = etime()
    elapsed = end - start
    return elapsed

def test(name):
    """Tests the given function with a range of values for n.
    Returns a list of ns and a list of run times.
    """
    # look up the string (name) and get the function object
    f = eval(name)

    # depending on which function we are testing, we need to
    # use a different order of magnitude for (n)
    d = dict(LinearMap=1000,
             BetterMap=1000,
             HashMap=1000)
    factor = d[name]

    # test (f) over a range of values for (n)
    ns = []
    ts = []
    for i in range(2, 25):
        n = factor * i
        mapObj = f()
        t = testAddMap(mapObj, n)
        print n, t
        t2 = testGetMap(mapObj, n)
        ns.append(n)
        ts.append(t2)
    return ns, ts


def make_figure(funcs, scale='log', exp=1.0, filename=''):
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('n')
    pyplot.ylabel('run time (s)')

    colors = ['blue', 'orange', 'green']
    for func, color in zip(funcs, colors):
        data = test(func)
        plot(*data, label=func, color=color, exp=exp)

    pyplot.legend(loc=4)

    if filename:
        save(filename, 'pdf')
    else:
        pyplot.show()



def main(script):
    make_figure(['LinearMap', 'BetterMap', 'HashMap'], exp=1.0, filename='')

if __name__ == '__main__':
    import sys
    main(*sys.argv)