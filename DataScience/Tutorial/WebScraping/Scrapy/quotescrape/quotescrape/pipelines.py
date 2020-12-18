# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class QuotescrapePipeline:
    def __init__(self):
        self.create_database()
        self.create_tables()

    def process_item(self, item, spider):
        self.fill_tables(item)
        return item

    def create_database(self):
        self.conn = sqlite3.connect('./quotes.db')

    def create_tables(self):
        self.conn.execute('''DROP TABLE IF EXISTS quotes''')
        self.conn.execute('''CREATE TABLE quotes(
                            quote text primary key,
                            author text
                        )''')

        self.conn.execute('''DROP TABLE IF EXISTS tags''')
        self.conn.execute('''CREATE TABLE quotes(
                            quote text,
                            tag text
                        )''')

    def fill_tables(self, item):
        self.conn.execute('''INSERT INTO quotes values(?, ?)''', (item['quote'], item['author']))
        for tag in item['tags']:
            self.conn.execute('''INSERT INTO tags values(?, ?)''', (item['quote'], tag))
        self.conn.commit()
