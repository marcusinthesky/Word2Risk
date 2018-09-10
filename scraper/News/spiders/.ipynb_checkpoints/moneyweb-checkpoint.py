import scrapy
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup


class moneywebSpider(scrapy.Spider):
    name = "moneyweb"
    
    def __init__(self, *a, **kw):
        super(moneywebSpider, self).__init__(*a, **kw)
        path = os.path.join(os.path.expanduser("~"),"Documents","NMRQL","Scraper","News","companies.csv")
        self.companies = pd.read_csv(path).date.tolist()
        self.next_tag = 'html body#gsr.srp.tbo.vasq div#main div#cnt.big div.mw div#rcnt div.col div#center_col div div#foot span#xjs div#navcnt table#nav tbody tr td.b.navend a#pnnext.pn span::text'
        self.site = "www.moneyweb.co.za/news/"

    def start_requests(self):
        for company in self.companies:
            self.pages = 1
            
            while True:        
                l = f'https://www.bing.com/search?q=site%3a+{self.site}+"{company.replace(" ", "+")}"&rf=1&qpvt=site%3a+{self.site}+"+{company.replace(" ", "+")}+"&lf=&first={self.pages}0'
                r = requests.get(l)
                soup = BeautifulSoup(r.text, 'html.parser')
                pages_list = [int(i.text) for i in soup.find_all('a', attrs='sb_bp') if str.isnumeric(i.text)]
                
                if self.pages in pages_list:
                    self.pages += 1
                    yield scrapy.Request(l, callback=self.get_links_parse, meta={'company':company})
                else:
                    break
    
    def get_links_parse(self, response):
        company = response.meta['company']
        for url in response.css(f'a[href^="https://{self.site}"]::attr(href)').extract():
            yield scrapy.Request(url, callback=self.xyield_text_parse, meta={'company':company, 'url': url})
    
    def xyield_text_parse(self, response):
        company = response.meta['company']
        url = response.meta['url']
        date = response.css('meta[property$="time"]::attr(content)').extract_first()
        text = ' '.join(response.css('div.article-content p::text').extract())
        
        yield {
            'source': url,
            'company': company,
            'date':date,
            'text': text
        }