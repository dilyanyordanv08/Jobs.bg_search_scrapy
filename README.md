# Jobs.bg_search_scrapy

ScraperNameSpider
This is a web scraping script that extracts job postings related to the Python language from Jobs.bg.

Dependencies
Python 3
Scrapy
Pandas
Usage
Install the dependencies by running the command pip install scrapy pandas.
Open your terminal and navigate to the folder where the script is located.
Run the script by typing scrapy runspider ScraperNameSpider.py -o jobs.csv in your terminal.
The script will create a CSV file named "jobs.csv" in the same folder as the script.
How it works
The script accesses the Jobs.bg website and extracts information about job postings related to the Python language. It then saves the information to a CSV file named "jobs.csv".

The following information is extracted for each job posting:

Position
Company name
Location
Number of employees
Today's date
Date posted
Job URL
Work from home
Skills list
Skills with no images
The script uses Scrapy to crawl the website and extract the necessary information. Pandas is used to convert the date column from object to datetime.

