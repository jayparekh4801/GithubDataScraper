# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import scrapy


class GithubseekerPipeline:
    def __init__(self) :
        connector = MongoClient('mongodb://localhost')
        database = connector['gitbase']
        self.collection = database['userData']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        # return item
