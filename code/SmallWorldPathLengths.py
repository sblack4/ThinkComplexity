"""
Excercise 4-5
"""

import matplotlib.pyplot as pyplot
from SmallWorldGraph import SmallWorldGraph, name_generator, Vertex



def generateData(pStart, pMultiplier):
    l0 = (52/(2*5))
    x = []
    y = []
    while(pStart<1):
        names = name_generator()
        vs = [Vertex(names.next()) for c in range(52)]
        graph = SmallWorldGraph(vs, 5, pStart)
        x.append(pStart)
        y.append(graph.char_length()/l0)
        pStart *= pMultiplier
    return [x, y]

def makeFigure(pStart, pMultiplier):
    pyplot.clf()
    pyplot.xscale('log')
    pyplot.yscale('linear')
    pyplot.title('L(p)/L(0) vs p')
    pyplot.xlabel('p')
    pyplot.ylabel('L(p)/L(0)')
    [x, y] = generateData(pStart, pMultiplier)
    pyplot.scatter(x, y)
    pyplot.show()


def main(script, pStart=0.001, pMultiplier=1.1):
    makeFigure(pStart, pMultiplier)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
