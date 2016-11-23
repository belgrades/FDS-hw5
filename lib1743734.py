import numpy as np


def charfreq(filename, filtering):
    """
    Calculate the relative frequencies of the characters appearing in the file filename.
    :param filename: The path filename to the book.
    :param filtering: The characters we need to count.
    :return:
    """
    from collections import Counter

    file = open(filename, "r", encoding="UTF-8")
    lines = file.read()

    counter = Counter((character for character in filter(lambda x: x in filtering, lines)))
    values = [counter[value] for value in filtering]
    n = sum(values)

    return np.array([character/n for character in values])


def euc(x, y):
    """
    Calculates the euclidean distance between two numpy arrays.
    :param x: Vector x.
    :param y: Vector y.
    :return: Euclidean distance between x and y.
    """
    # TODO: Add math doc.
    return np.sqrt(np.sum((x-y)**2))


def cldist(c1, c2):
    """
    Calculates the minimum distance between all the elements in clusters c1 and c2. Using a generator for efficiency.
    A cluster ci i={1, 2} is a list of numpy arrays.
    :param c1: Cluster 1.
    :param c2: Cluster 2.
    :return: The minimum euclidean distance between c1 and c2.
    """
    return min(euc(x, y) for x in c1 for y in c2)


def closest(L):
    """
    Calculates the indexes i, j of the minimum distance between clusters in L.
    L should be a list of numpy arrays.
    :param L: List of clusters.
    :return: The indexes of the clusters that have minimum distance between each other.
    """
    n = len(L)
    mind = np.infty
    pair = (-1, -1)

    for i in range(n-1):
        for j in range(i+1, n):
            dist_ij = cldist(L[i], L[j])
            if dist_ij < mind:
                mind = dist_ij
                pair = (i, j)
    return pair


def remove_array(np_list, arr):
    """
    Issue using list.remove() from python core.
    Solved in: http://stackoverflow.com/questions/3157374/how-do-you-remove-a-numpy-array-from-a-list-of-numpy-arrays
    Using solution from Justin Peel
    :param np_list: List of numpy arrays.
    :param arr: The array I want to remove.
    :return: The list np_list without arr.
    """
    ind = 0
    size = len(np_list)

    while ind != size and not np.array_equal(np_list[ind], arr):
        ind += 1

    if ind != size:
        np_list.pop(ind)


def single_linkage(D, k=2):
    """
    Implementation of the single-linkage clustering algorithm using list of numpy arrays.
    :param D: List of clusters.
    :param k: Number of clusters.
    :return: Array or list whose i-th entry is the cluster ID of the i-th element.
    """
    n = len(D)
    clusters = [[i] for i in range(n)]

    while len(D) > k:
        i, j = closest(D)
        c1, c2 = D[i], D[j]
        idx1, idx2 = clusters[i], clusters[j]

        clusters.remove(idx1)
        clusters.remove(idx2)
        clusters.append(idx1+idx2)

        remove_array(D, c1)
        remove_array(D, c2)
        D.append(c1+c2)

    return clusters
