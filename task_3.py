import multiprocessing
import sys


def search_keyword(filename, keyword):
    with open(filename, 'r') as file:
        content = file.read()
        if keyword in content:
            return True
        else:
            return False


if __name__ == '__main__':

    if len(sys.argv) < 3:
        sys.exit(1)
    keyword = sys.argv[1]
    filenames = sys.argv[2:]
    pool = multiprocessing.Pool()
    results = pool.map(lambda filename: search_keyword(
        filename, keyword), filenames)
    pool.close()
    pool.join()
    for filename, result in zip(filenames, results):
        if result:
            print(f"Keyword '{keyword}' found in file '{filename}'")
        else:
            print(f"Keyword '{keyword}' not found in file '{filename}'")
