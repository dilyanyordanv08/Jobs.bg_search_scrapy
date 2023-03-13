# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscraperItem(scrapy.Item):
    position = scrapy.Field()
    company_name = scrapy.Field()
    location = scrapy.Field()
    number_of_employees = scrapy.Field()
    todays_date = scrapy.Field()
    date_posted = scrapy.Field()
    job_url = scrapy.Field()
    work_from_home = scrapy.Field()
    skills_list = scrapy.Field()
    skills_no_img = scrapy.Field()
