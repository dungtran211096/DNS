from multiprocessing import Pool


def process_line(line):
    return line.strip().split(',')


def read_file(filename):
    pool = Pool(4)
    with open(filename) as source_file:
        # chunk the work into batches of 4 lines at a time
        results = pool.map(process_line, source_file, 4)
        return results


