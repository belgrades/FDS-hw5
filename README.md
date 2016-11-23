# FDS-hw5
Clustering of books using char frequencies

Class: Nov 18, 2016.
The goal of today's class is to re-implement a clustering algorithm, "single linkage", breaking it down into a set of ancillary functions. They are given as exercises below.

EXERCISE: write a function charfreq(path, filter) that reads the file 'path' and returns, in a numpy array, the relative frequencies of the characters appearing in the file, considering only those in the string 'filter'. Example:
In [130]: charfreq("it-1.txt", "aeiou")
Out[130]: array([ 0.24,  0.24,  0.24,  0.22,  0.06])

EXERCISE: obtain the vectors of relative frequencies of the wovels "aeiou", for the books it-1.txt, it-2.txt, ..., and plot some of them as histograms with matplotlib.

EXERCISE: write a function euc(x,y) that computes the Euclidean distance between two points x and y in R^n, given as numpy arrays of n elements.

EXERCISE: now suppose we want to cluster points. Each cluster is represented as a list. Write a function cldist(c1, c2) that computes the (Euclidean) distance between the two clusters c1 and c2. Each cluster is a list of NumPy arrays (= points in R^n).

EXERCISE: Write a function closest(L) that, given a list of clusters, returns the indices of the two distinct clusters that are closest to each other.

EXERCISE: rewrite single_linkage(D, k) using loops and representing clusters as lists. It will receive a list of points in R^n, as numpy arrays. It will return a list of lists, one for each cluster, specifying the ids of the points it contains. For example, this is what you should obtain when L is produced from the 8 books available in zip format on the website of the course:
 In[1]: single_linkage(L, 4)
 Out[1]: [[0, 4], [1, 5], [2, 6], [3, 7]]

EXERCISE: write a script that takes from command line a list of file names and an integer number, and then uses single_linkage to cluster the files by wovel frequencies, using the specified number of clusters. It will print the clustered file names in output. Example:
 $ ipython wovclust.py *-*.txt 4
 cluster:  ['da-1.txt', 'da-2.txt']
 cluster:  ['en-1.txt', 'en-2.txt']
 cluster:  ['fr-1.txt', 'fr-2.txt']
 cluster:  ['it-1.txt', 'it-2.txt']
