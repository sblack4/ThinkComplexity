"""

"""

import matplotlib.pyplot as plt
from SmallWorldGraph import SmallWorldGraph, name_generator
from Graph import Vertex
from time import clock


def makeGraph(n='52', k='5', p='0.1'):
    #create n Vertices
    n = int(n)
    k = int(k)
    p = float(p)

    names = name_generator()
    vs = [Vertex(names.next()) for c in range(n)]

    # create a graph
    g = SmallWorldGraph(vs, k, p)
    start = clock()
    g.char_length()
    charLength1 = clock() - start

    start = clock()
    g.char_length2()
    charLength2 = clock() - start
    
    start = clock()
    g.char_length3()
    charLength3 = clock() - start

    start = clock()
    g.char_length4()
    charLength4 = clock() - start
    return charLength1, charLength2, charLength3, charLength4

def generateNumbersForEdges(nStart=10, nEnd=100):
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    y = []
    for n in range(nStart, nEnd, 2):
        a,b,c,d = makeGraph(n)
        y.append(n)
        x1.append(a)
        x2.append(b)
        x3.append(c)
        x4.append(d)
        print "n %s, times: %s %s %s %s " % (n, a, b, c ,d)
    title = '%d through %d  Nodes vs Run-time for 4 different Algorithms' % (nStart, nEnd)
    xAxis = 'Number of Edges'
    plotGraph(y, x1, x2, x3, x4, title, xAxis)

def generateNumbersForK(kStart=1, kEnd=45):
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    y = []
    for k in range(kStart, kEnd):
        a,b,c,d = makeGraph(k=k)
        y.append(k)
        x1.append(a)
        x2.append(b)
        x3.append(c)
        x4.append(d)
        print "k %s, times: %s %s %s %s " % (k, a, b, c ,d)
    title = '%d through %d K vs Run-time for 4 different Algorithms' % (kStart, kEnd)
    xAxis = 'k coefficient (mean degree of edges)'
    plotGraph(y, x1, x2, x3, x4, title, xAxis)

def plotGraph(y, x1, x2, x3, x4, title, xAxis):

    fig = plt.figure()
    plt.title(title)
    plt.ylabel('O(n) for different algorithms')
    plt.xlabel(xAxis)
    ax1 = fig.add_subplot(111)

    ax1.scatter(y,x1, s=20, c='b', marker="s", label='Dijkstra''s algorithm')
    ax1.scatter(y,x2, s=20, c='r', marker="o", label='squaring algorithm')
    ax1.scatter(y,x3, s=20, c='c', marker="v", label='Floyd-Warshall algorithm')
    ax1.scatter(y,x4, s=20, c='m', marker="^", label='recursive Floyd-Warshall')
    plt.legend(loc='upper left');
    plt.show()


def main(script):
    # generateNumbersForEdges()
    generateNumbersForK()


if __name__ == '__main__':
    import sys
    main(*sys.argv)