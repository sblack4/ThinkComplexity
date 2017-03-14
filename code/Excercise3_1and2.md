### Exercise 1  Read the Wikipedia page on Big-Oh notation at [http://en.wikipedia.org/wiki/Big_O_notation](http://en.wikipedia.org/wiki/Big_O_notation) and answer the following questions:
##### 1. What is the order of growth of n<sup>3</sup> + n<sup>2</sup>? What about 1000000 n<sup>3</sup> + n<sup>2</sup>? What about n<sup>3</sup> + 1000000 n<sup>2</sup>?
O(n<sup>3</sup>)
##### 2. What is the order of growth of (n<sup>2</sup> + n) * (n + 1)? Before you start multiplying, remember that you only need the leading term.
O(n<sup>3</sup>)
##### 3. If f is in O(g), for some unspecified function g, what can we say about a f + b?
O(a*g+b) = O(g)
##### 4. If f1 and f2 are in O(g), what can we say about f1 + f2?
O(2*g) = O(g)
##### 5. If f1 is in O(g) and f2 is in O(h), what can we say about f1 + f2?
O(g+h)  
##### 6. If f1 is in O(g) and f2 is O(h), what can we say about f1 * f2?
O(g*h)  

### Exercise 2  Read the Wikipedia page on sorting algorithms at [http://en.wikipedia.org/wiki/Sorting_algorithm](http://en.wikipedia.org/wiki/Sorting_algorithm) and answer the following questions:
##### 1. What is a “comparison sort?” What is the best worst-case order of growth for a comparison sort? What is the best worst-case order of growth for any sort algorithm?

##### 2. What is the order of growth of bubble sort, and why does Barack Obama think it is “the wrong way to go?”
##### 3. What is the order of growth of radix sort? What preconditions do we need to use it?
##### 4. What is a stable sort and why might it matter in practice?
##### 5. What is the worst sorting algorithm (that has a name)?
##### 6. What sort algorithm does the C library use? What sort algorithm does Python use? Are these algorithms stable? You might have to Google around to find these answers.
##### 7. Many of the non-comparison sorts are linear, so why does does Python use an O(n logn) comparison sort?