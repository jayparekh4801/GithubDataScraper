import scrapy
from scrapy.loader import ItemLoader
from ..items import GithubseekerItem
import mysql.connector
import glob
import os
import csv
import pandas
from openpyxl import Workbook
import pymongo


class GithubseekerSpider(scrapy.Spider):
    name = 'githubseeker'
    allowed_domains = ['https://github.com']
    start_urls = ['https://github.com/']

    def __init__(self, name = None, userName = "jayparekh4801", **kwargs) :
        self.start_urls = ["https://github.com/" + userName]

    def parse(self, response):
        l = ItemLoader(item = GithubseekerItem(), response=response)    
        name = response.xpath('//span[@itemprop = "name"]/text()').get()
        userName = response.xpath('//span[@itemprop = "additionalName"]/text()').get()
        image_urls = response.xpath('//div/a/img/@src').get()
        biodata = response.xpath('//div[@class = "d-flex flex-column"]/div[2]/div/div/text()').get()
        current_work = response.xpath('//span[@class = "p-org"]/div/text()').get()
        work_loc = response.xpath('//span[@class = "p-label"]/text()').get()
        no_repos = response.xpath('//a[@class = "UnderlineNav-item"][1]/span[1]/text()').get()
        lis_popular_repos = response.xpath('//span[@class = "repo"]/text()').get()
        tot_commits = response.xpath('//h2[@class = "f4 text-normal mb-2"]/text()').get()

        l.add_value('name', name)
        l.add_value('userName', userName)
        l.add_value('image_urls', image_urls)
        l.add_value('biodata', biodata)
        l.add_value('current_work', current_work)
        l.add_value('work_loc', work_loc)
        l.add_value('no_repos', no_repos)
        l.add_value('lis_popular_repos', lis_popular_repos)
        l.add_value('tot_commits', tot_commits)
        yield l.load_item() 
        
    
    def close(self, reason) :
        # csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)

        #  code to put data in mysql database 
        # mydb = mysql.connector.connect(
        #     host = "127.0.0.1",
        #     user = "root",
        #     password = "vnhmhJi#7ms",
        #     database = "scrapy"
        # )
        # mycursor = mydb.cursor()
        # createTable = "CREATE TABLE GITDATA(name VARCHAR(200), userName VARCHAR(200), current_work VARCHAR(200), work_loc VARCHAR(200), no_repos VARCHAR(200), tot_commits VARCHAR(200))"
        # mycursor.execute(createTable)
        # csv_data = csv.reader(open(csv_file))
        # row_count = 0
        # for row in csv_data:
        #     if row_count != 0 :
        #         insertInto = ("INSERT IGNORE INTO GITDATAo(name, userName, image_urls, biodata, current_work, work_loc, no_repos, lis_popular_repos, tot_commits) VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        #         mycursor.execute(insertInto, row)
        #     row_count += 1

        # mydb.commit()
        # mycursor.close()

        #  code to put data in mongodb database

        jl_file = max(glob.iglob('*.jl'), key = os.path.getctime)
        mongo_connector = pymongo.MongoClient("mongodb://localhost/")
        database = mongo_connector['gitDatabase']
        collection = database['gitUserData']

        with open(jl_file) as fp :
            for row in fp.readlines() :
                gitRow = {"data" : row}
                collection.insert_one(gitRow)
            
