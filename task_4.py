import concurrent.futures
import sys


def search_keyword_in_file(filename, keyword):
    with open(filename, 'r') as file:
        contents = file.read()
        if keyword in contents:
            return filename


def main():

    if len(sys.argv) < 3:
        return

    keyword = sys.argv[1]
    filenames = sys.argv[2:]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = []
        for filename in filenames:
            result = executor.submit(search_keyword_in_file, filename, keyword)
            results.append(result)

        for result in concurrent.futures.as_completed(results):
            filename = result.result()
            if filename:
                print(f"Keyword found in file: {filename}")


if __name__ == '__main__':
    main()
