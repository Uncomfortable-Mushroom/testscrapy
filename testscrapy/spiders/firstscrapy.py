#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import scrapy

class firstscrapy(scrapy.Spider):
    name = "firstscrapy"
    start_urls=['http://lab.scrapyd.cn' ]

    def parse(self, response):
        list=response.css('div.quote')
        for mingyan in list:
            text=mingyan.css('.text::text').extract_first()
            author=mingyan.css('.author::text').extract_first()
            tags=mingyan.css('.tags .tag::text').extract()
            tags = ','.join(tags)
            fileName = '%s-语录.txt' % author
            with open(fileName, "a+") as f:
                f.write(text)
                f.write('\n-----\n')
                f.write('标签：' + tags)
                f.write('\n-----\n')
                f.close()
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)