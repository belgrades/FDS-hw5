import sys
import lib1743734 as lib


def main():
    books = sys.argv[1:-2]
    filter_param = sys.argv[-2]
    k = int(sys.argv[-1])

    dist_books = [[lib.charfreq(book, filter_param)] for book in books]

    for cluster in lib.single_linkage(dist_books, k):
        for i in range(len(cluster)):
            cluster[i] = books[cluster[i]]
        print(cluster)

if __name__ == '__main__':
    main()
