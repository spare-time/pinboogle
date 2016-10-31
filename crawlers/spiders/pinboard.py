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
        self.logger.info("[PINBOARD_SPIDER] Start URL: %s" % self.start_urls[0])

    def parse(self, response):
        # fetches json representation of bookmarks instead of using css or xpath
        bookmarks = re.findall('bmarks\[\d+\] = (\{.*?\});', response.body.decode('utf-8'), re.DOTALL | re.MULTILINE)
        self.logger.info("[PINBOARD_SPIDER] Bookmarks on this page: %d" % len(bookmarks))

        for bookmark in bookmarks:
            yield self.parse_bookmark(json.loads(bookmark))

        next_page = response.css('a#top_later::attr(href)').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            self.logger.info("[PINBOARD_SPIDER] Fetching next page: %s" % next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_bookmark(self, bookmark):
        pin = PinboardLinkItem()

        pin['link_id'] = bookmark['id'] 
        pin['link_url'] = bookmark['url']
        pin['link_url_slug'] = bookmark['url_slug']
        pin['title'] = bookmark['title']
        pin['description'] = bookmark['description']

        created_at = datetime.datetime.strptime(bookmark['created'],'%Y-%m-%d %H:%M:%S')
        pin['created_at'] = created_at.isoformat()

        pin['saved_by_others'] = bookmark['url_count']
        pin['tags'] = bookmark['tags']
        pin['private'] = bookmark['private']
        pin['to_read'] = bookmark['toread']
        pin['author'] = bookmark['author']

        request = scrapy.Request(pin['link_url'], callback=self.parse_external_link)
        request.meta['pin'] = pin # this passes over the pin item to the request
        return request

    def parse_external_link(self, response):
        pin = response.meta['pin']

        pin['html_fetch_date'] = datetime.datetime.utcnow().isoformat() 
        pin['html_code'] = response.status
        pin['html_content'] = ""
        pin['html_content_size'] = 0
        if response.body:
            soup = BeautifulSoup(response.body, 'html.parser')
            # http://stackoverflow.com/questions/22799990/beatifulsoup4-get-text-still-has-javascript
            for script in soup(["script", "style"]):
                script.extract()
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            pin['html_content'] = text
            pin['html_content_size'] = len(pin['html_content'])

        return pin
