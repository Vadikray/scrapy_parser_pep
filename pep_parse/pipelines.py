import csv
from collections import defaultdict
from datetime import datetime

from constants import RESULTS, DATETIME_FORMAT, FILENAME, BASE_DIR


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_path = self.results_dir / FILENAME.format(
            time=datetime.now().strftime(DATETIME_FORMAT))
        with open(file_path, mode='w',
                  encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile, dialect='excel-tab')
            writer.writerows([
                ['Статус', 'Количество'],
                *(self.results.items()),
                ['Total', sum(self.results.values())]
            ])
