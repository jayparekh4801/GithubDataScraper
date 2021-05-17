# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubseekerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    userName = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    biodata = scrapy.Field()
    current_work = scrapy.Field()
    work_loc = scrapy.Field()
    no_repos = scrapy.Field()
    lis_popular_repos = scrapy.Field()
    tot_commits = scrapy.Field()

