import scrapy
from time import sleep

# scrapy runspider -o books.csv indeedscrape.py

class IndeedSpider(scrapy.Spider):
    name = "indeedspider"
    start_urls = ["https://www.indeed.com/q-rn-l-Denver,-CO-jobs.html"]
    
    def parse(self, response):
         salary = response.css(".salary::text").extract_first()
         org = response.css(".company > a::text").extract_first()
         for job in response.css(".jobsearch-SerpJobCard"):
            yield {
                 'title': job.css(".turnstileLink::attr(title)").extract_first(),
                 'company': org.strip(),
                 'location': job.css(".location::text").extract_first(),
                 'pay': salary.strip(),
                 'age': job.css(".date").extract_first()

                 }
           
            next = response.css('.pn').extract_first()
            page = response.css('.pagination > a:last-child::attr(href)').extract_first()
            if next:
               sleep(2)
               yield response.follow(page, self.parse)