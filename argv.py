import sys
import getopt


def k(argv):
    mangaName = ''

    try:
        opts, args = getopt.getopt(argv, "hn:a", ["mname"])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -n <manganame> -a')
            sys.exit()
        elif opt in("-n", "--mname"):
            mangaName = arg

    return mangaName
    # if __name__ == "__main__":
    # k(sys.argv[1:])
