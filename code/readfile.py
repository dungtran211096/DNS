from multiprocessing import Pool


class ReadFile():
    def __init__(self):
        self.filename = "/media/dung/Dung Tran/GSLB/geoip_data.dat"

    def process_line(self, line):
        return line.strip().split(',')

    def read_file(self):
        pool = Pool(4)
        with open(self.filename) as source_file:
            # chunk the work into batches of 4 lines at a time
            results = pool.map(self.process_line, source_file, 4)
            return results


