# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import scrapy
import os


class GithubseekerPipeline:
    def __init__(self) :
        connector = MongoClient('mongodb://localhost')
        database = connector['gitbase']
        self.collection = database['userData']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

class GithubImageNaemChanger : 
    def process_item(self, item, spider) :
        os.chdir('/Users/jayparekh/Documents/Scrapy_Tutorial/GithubSeeker/images')

        if(item['images'][0]['path'] != None) :
            new_path = 'full/' + item['userName'][0] + '.jpg'
            os.rename(item['images'][0]['path'], new_path)
