

## Exercise 1  
>Read the Wikipedia page about graphs at [http://en.wikipedia.org/wiki/Graph_(mathematics)](http://en.wikipedia.org/wiki/Graph_(mathematics)) and answer the following questions:

>What is a simple graph? In the rest of this section, we will be assuming that all graphs are simple graphs. This is a common assumption for many graph algorithms—so common it is often unstated.   
A unidirectional graph where multiple edges and loops are not allowed

>What is a regular graph? What is a complete graph? Prove that a complete graph is regular.
A regular graph has nodes where each node has the same number of edges.  A complete graph has nodes which are all connected.  
A complete graph is regular proof: by definition a complete graph has nodes which all have n-1 (the same number) vertices.

>What is a path? What is a cycle?  
A path is graph where you can hit each node and verticie once.  A cycle is path where you end up on the same vertice you started from.  

>What is a forest? What is a tree? Note: a graph is connected if there is a path from every node to every other node. 
A forest is a graph with no cycles.  


## Exercise 2  
>In this exercise you write methods that will be useful for many of the Graph algorithms that are coming up.
>Download thinkcomplex.com/[GraphCode.py](GraphCode.py), which contains the code in this chapter. Run it as a script and make sure the test code in main does what you expect.
>Make a copy of GraphCode.py called [Graph.py](Graph.py). Add the following methods to Graph, adding test code as you go.
>Write a method named get_edge that takes two vertices and returns the edge between them if it exists and None otherwise. Hint: use a try statement.
>Write a method named remove_edge that takes an edge and removes all references to it from the graph.
>Write a method named vertices that returns a list of the vertices in a graph.
>Write a method named edges that returns a list of edges in a graph. Note that in our representation of an undirected graph there are two references to each edge.
>Write a method named out_vertices that takes a Vertex and returns a list of the adjacent vertices (the ones connected to the given node by an edge).
>Write a method named out_edges that takes a Vertex and returns a list of edges connected to the given Vertex.
>Write a method named add_all_edges that starts with an edgeless Graph and makes a complete graph by adding edges between all pairs of vertices.
>Test your methods by writing test code and checking the output. Then download thinkcomplex.com/GraphWorld.py. GraphWorld is a simple tool for generating visual representations of graphs. It is based on the World class in Swampy, so you might have to install Swampy first: see thinkpython.com/swampy.
>Read through GraphWorld.py to get a sense of how it works. Then run it. It should import your Graph.py and then display a complete graph with 10 vertices.  

See [GraphCode.py](GraphCode.py) and [Graph.py](Graph.py)  (mostly his code)


## Exercise 3  
>Write a method named add_regular_edges that starts with an edgeless graph and adds edges so that every vertex has the same degree. The degree of a node is the number of edges it is connected to.
>To create a regular graph with degree 2 you would do something like this:
> ```python
>vertices = [ ... list of Vertices ... ]
>g = Graph(vertices, [])
>g.add_regular_edges(2)
> ```
>It is not always possible to create a regular graph with a given degree, so you should figure out and document the preconditions for this method.
>To test your code, you might want to create a file named GraphTest.py that imports Graph.py and GraphWorld.py, then generates and displays the graphs you want to test.  

See [GraphTest.py](GraphTest.py) (his code)


## Exercise 4  
>Create a file named RandomGraph.py and define a class named RandomGraph that inherits from Graph and provides a method named add_random_edges that takes a probability p as a parameter and, starting with an edgeless graph, adds edges at random so that the probability is p that there is an edge between any two nodes.  

See [RandomGraph.py](RandomGraph.py) which is mostly his


## Exercise 5  
>Write a Graph method named is_connected that returns True if the Graph is connected and False otherwise.  

See [Graph.py](Graph.py) 


## Exercise 6  
>One of the properties that displays this kind of transition is connectedness. For a given size n, there is a critical value, p*, such that a random graph G(n, p) is unlikely to be connected if p < p* and very likely to be connected if p > p*.

>Write a program that tests this result by generating random graphs for values of n and p and computes the fraction of them that are connected.
See [RandomGraphTester.py](RandomGraphTester.py)

>How does the abruptness of the transition depend on n?
the value of n does not affect the transition as much as the value of p.  


## Exercise 7  
>Write a generator that yields an infinite sequence of alpha-numeric identifiers, starting with a1 through z1, then a2 through z2, and so on.

[Excercise2_7.py](Excercise2_7.py)
