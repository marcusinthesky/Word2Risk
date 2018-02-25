# -*- coding: utf-8 -*-
import scrapy
import os
import json

class MoneywebSensSpider(scrapy.Spider):
    name = "moneyweb_sens"

    def __init__(self, *a, **kw):
        super(MoneywebSensSpider, self).__init__(*a, **kw)

    def start_requests(self):
        base_url = 'https://www.moneyweb.co.za/tools-and-data/moneyweb-sens/'
        yield scrapy.Request(url=base_url, callback=self.parse_home)
   
    def parse_home(self,response):
        pages = int(response.css('div div#page-container.container div#body-content.block.m1010 div#left-content.col-lg-8.col-md-8 div.pagination.col-lg-12.col-md-12.col-sm-12.col-xs-12.markets-widget.m1010 div.block.bottom.m0505 a.page-numbers::text')[-2].extract().replace(',', ''))
        base_url = 'https://www.moneyweb.co.za/tools-and-data/moneyweb-sens/'
        for pages in range(1,pages):
            url = base_url + 'page/' + str(pages)
            yield scrapy.Request(url=url, callback=self.parse_pages)

    def parse_pages(self, response):

        reports = response.css('div div#page-container.container div#body-content.block.m1010 div#left-content.col-lg-8.col-md-8 div.sens-row div.col-lg-7.col-md-7.col-sm-7.col-xs-12 a::attr(href)').extract()
        
        date = response.css('div div#page-container.container div#body-content.block.m1010 div#left-content.col-lg-8.col-md-8 div.sens-row div.col-lg-2.col-md-2.col-sm-2.col-xs-12.clickacompany-date time::attr(datetime)').extract()
        
        
        rep_date = list(zip(reports,date))
        
        for i in rep_date:
            item = {'date':i[1]}
            yield scrapy.Request(url=i[0], callback=self.parse_article, meta={'item':item})

    def parse_article(self, response):
        item = response.meta['item']
        date = item['date']
        section = 'sens'
        title = response.css('h1::text').extract_first()
        texts = '-'.join(list(map(lambda x: x.strip(),response.css('p::text').extract()[:-12])))
        yield {
            'title':title, 
            'section':section,
            'date':date, 
            'text':texts,
            'url':response.url,
        }