# -*- coding: utf-8 -*-
import scrapy


class PinboardSpider(scrapy.Spider):
    name = "pinboard"
    allowed_domains = ["pinboard.in"]
    start_urls = (
        'http://www.pinboard.in/',
    )

    def parse(self, response):
        pass
