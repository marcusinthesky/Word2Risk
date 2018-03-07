# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "bloomberg"

    def start_requests(self):
        url = 'https://www.bloomberg.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        #for quote in response.css('div.quote'):
        
        yield {
            'time': response.css('time::attr(datetime)').extract_first(),
            'body': response.css('p::text')[8:].extract(),
            'url': response.url,
        }

        next_page = response.css('a::attr(href)').extract()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
    '''
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            #Can use response.css('title::text')[0].extract() to get either the string or without the [0] to get a list of the text.  
        self.log('Saved file %s' % filename)
    
    '''
    