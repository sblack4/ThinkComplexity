## Exercise 1  Read the Wikipedia page on Big-Oh notation at [http://en.wikipedia.org/wiki/Big_O_notation](http://en.wikipedia.org/wiki/Big_O_notation) and answer the following questions:

1. What is the order of growth of n<sup>3</sup> + n<sup>2</sup>? What about 1000000 n<sup>3</sup> + n<sup>2</sup>? What about n<sup>3</sup> + 1000000 n<sup>2</sup>?  
O(n<sup>3</sup>)

2. What is the order of growth of (n<sup>2</sup> + n) * (n + 1)? Before you start multiplying, remember that you only need the leading term.  
O(n<sup>3</sup>) 

3. If f is in O(g), for some unspecified function g, what can we say about a f + b?  
O(a*g+b) = O(g)

4. If f1 and f2 are in O(g), what can we say about f1 + f2?  
O(2*g) = O(g)

5. If f1 is in O(g) and f2 is in O(h), what can we say about f1 + f2?  
O(g+h)  

6. If f1 is in O(g) and f2 is O(h), what can we say about f1 * f2?  
O(g*h)  



## Exercise 2  Read the Wikipedia page on sorting algorithms at [http://en.wikipedia.org/wiki/Sorting_algorithm](http://en.wikipedia.org/wiki/Sorting_algorithm) and answer the following questions:

1. What is a “comparison sort?” What is the best worst-case order of growth for a comparison sort? What is the best worst-case order of growth for any sort algorithm?  
a type of sorting algorithm that compares two pieces of data.  Best worst-case: unshuffle sort kn, for any spreadsort at n*(k/s + d)

2. What is the order of growth of bubble sort, and why does Barack Obama think it is “the wrong way to go?”  
it takes a value and then compares it up or down the list, so lots of comparisons * lots of values = lots of time!

3. What is the order of growth of radix sort? What preconditions do we need to use it?  
it sorts the data by individual digits so the data must have integer keys 

4. What is a stable sort and why might it matter in practice?  
maintain relative order of elements with equal keys.  multiple different sorted versions of original list

5. What is the worst sorting algorithm (that has a name)?  
Bogosort

6. What sort algorithm does the C library use? What sort algorithm does Python use? Are these algorithms stable? You might have to Google around to find these answers.  
a quicksort variant.  Timsort: Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort

7. Many of the non-comparison sorts are linear, so why does does Python use an O(n logn) comparison sort?    
because Tim knows best :hankey: 



## Exercise 3  
>Write a function called bisection that takes a sorted list and a target value and returns the index of the value in the list, if it’s there, or None if it’s not.
>Or you could read the documentation of the bisect module and use that!  
See [Excercise3_3.py](./code/Excercise3_3.py)


## Exercise 4  
>My implementation of HashMap accesses the attributes of BetterMap directly, which shows poor object-oriented design.
>The special method __len__ is invoked by the built-in function len. Write a __len__ method for BetterMap and use it in add.
>Use a generator to write BetterMap.iteritems, and use it in resize.   

See [MapSoln.py](./code/MapSoln.py)


## Exercise 5  
>A drawbacks of hashtables is that the elements have to be hashable, which usually means they have to be immutable. That’s why, in Python, you can use tuples but not lists as keys in a dictionary. An alternative is to use a tree-based map.
>Write an implementation of the map interface called TreeMap that uses a red-black tree to perform add and get in log time.  

See [Tree.py](./code/Tree.py)


## Exercise 6  
>Test the performance of LinearMap, BetterMap and HashMap; see if you can characterize their order of growth.
>You can download my map implementations from thinkcomplex.com/Map.py, and the code I used in this section from thinkcomplex.com/listsum.py.
>You will have to find a range of n that is big enough to show asymptotic behavior, but small enough to run quickly.  

See [Excercise3_6.py](./code/Excercise3_6.py)


## Exercise 7  
>Review the methods your wrote in Graph.py and see if any can be rewritten using list comprehensions.  

