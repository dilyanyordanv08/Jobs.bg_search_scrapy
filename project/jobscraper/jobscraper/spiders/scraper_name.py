import scrapy
import re
from datetime import datetime
from datetime import date


class ScraperNameSpider(scrapy.Spider):
    name = "scraper_name"
    start_urls = [
        'https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&techs%5B%5D=Python',
    ]

    def parse(self, response, **kwargs):
        # Get today's date
        today = date.today()
        date_string = today.strftime("%Y-%m-%d")
        
        for page in response.xpath('//ul[contains(@class, "page")]'):   
            for job in page.xpath('.//div[@class="mdc-card"]'):
                item = {}
                
                item['position'] = job.xpath('.//div[contains(@class, "card-title")]/span/text()').getall()
                item['company_name'] = job.xpath('.//div[@class="right"]/a/@title').get()
                item['location'] = job.css('div.card-info.card__subtitle::text').get().strip().replace(';', '')
                item['number_of_employees'] = job.xpath('.//div[contains(@class, "card__subtitle flex wrap more-details")]/span/text()').getall()
                item['todays_date'] = date_string

                item['date_posted'] = job.css('div.card-date::text').get().strip()
                if 'днес' in item['date_posted']:
                    todays_date = datetime.now().strftime("%Y-%m-%d")
                else:
                    todays_date = item["date_posted"]
                item['date_posted'] = todays_date

                item['job_url'] = job.css('div.left a').attrib['href']
                
                item['work_from_home'] = job.xpath('.//div[contains(@class, "card-info card__subtitle")]/span/text()').getall()
                if " Възможност" in item['work_from_home'] or " Дистанционно" in item['work_from_home']:
                    item['work_from_home'] = ["Home Office Possible" if x == " Възможност" else "Online Interview" for x in item['work_from_home']]
                    
                item['skills_list'] = job.xpath('.//div[contains(@class,"skill")]//img/@alt').extract()
                
                #item['skills_no_img'] = job.xpath('.//div[contains(@class, "skill-not-img")]/text()').extract()
                skills_no_img = job.xpath('.//div[contains(@class, "skill-not-img")]/text()').extract()
                if skills_no_img:
                    item['skills_no_img'] = skills_no_img
                else:
                    item['skills_no_img'] = ""

                yield item
