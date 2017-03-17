"""
Excercise 4-4
"""

import matplotlib.pyplot as pyplot
from SmallWorldGraph import SmallWorldGraph, name_generator, Vertex



def generateData(pStart, pMultiplier):
    c0 = 0.75
    x = []
    y = []
    while(pStart<1):
        names = name_generator()
        vs = [Vertex(names.next()) for c in range(52)]
        graph = SmallWorldGraph(vs, 5, pStart)
        x.append(pStart)
        y.append(graph.cluster_coef()/c0)
        pStart *= pMultiplier
    return [x, y]

def makeFigure(pStart, pMultiplier):
    pyplot.clf()
    pyplot.xscale('log')
    pyplot.yscale('linear')
    pyplot.title('C(p)/C(0) vs p')
    pyplot.xlabel('p')
    pyplot.ylabel('C(p)/C(0)')
    [x, y] = generateData(pStart, pMultiplier)
    pyplot.scatter(x, y)
    pyplot.show()


def main(script, pStart=0.001, pMultiplier=1.1):
    makeFigure(pStart, pMultiplier)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
