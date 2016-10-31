# -*- coding: utf-8 -*-
import scrapy
from crawlers.items import PinboardLinkItem
from bs4 import BeautifulSoup
import datetime, re, json

class PinboardSpider(scrapy.Spider):
    name = "pinboard"

    def __init__(self, user='lfcipriani', after='1', *args, **kwargs):
        super(PinboardSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://pinboard.in/u:%s/after:%s' % (user, after)]

    def parse(self, response):
        # fetches json representation of bookmarks instead of using css or xpath
        bookmarks = re.findall('bmarks\[\d+\] = (\{.*?\});', response.body.decode('utf-8'), re.DOTALL | re.MULTILINE)
        for bookmark in bookmarks:
            yield self.parse_bookmark(json.loads(bookmark))

    def parse_bookmark(self, bookmark):
        pin = PinboardLinkItem()

        pin['link_id'] = bookmark['id'] 
        pin['link_url'] = bookmark['url']
        pin['link_url_slug'] = bookmark['url_slug']
        pin['title'] = bookmark['title']
        pin['description'] = bookmark['description']

        created_at = datetime.datetime.strptime(bookmark['created'],'%Y-%m-%d %H:%M:%S')
        pin['created_at'] = created_at.isoformat()

        pin['saved_by_others'] = int(bookmark['url_count'])
        pin['tags'] = bookmark['tags']
        pin['private'] = bookmark['private']
        pin['to_read'] = bookmark['toread']
        pin['author'] = bookmark['author']

        return pin

