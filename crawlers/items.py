# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PinboardLinkItem(scrapy.Item):
    
    # fields that we get from pinboard
    link_id         = scrapy.Field()
    link_url        = scrapy.Field()
    link_url_slug   = scrapy.Field()
    title           = scrapy.Field()
    description     = scrapy.Field()
    created_at      = scrapy.Field()
    saved_by_others = scrapy.Field()
    tags            = scrapy.Field() #array of tags
    private         = scrapy.Field() 
    to_read         = scrapy.Field()
    author          = scrapy.Field()

    # fields that we get when fetching the link
    html_content      = scrapy.Field()
    html_code         = scrapy.Field()
    html_content_size = scrapy.Field()
    html_fetch_date   = scrapy.Field()

# JSON that's on pinboard results page
#{  
   #"id":"95383442",
   #"url":"http:\/\/lovelycharts.com\/",
   #"url_id":"112815",
   #"author":"lfcipriani",
   #"created":"2010-10-09 01:31:25",
   #"description":"",
   #"title":"Lovely Charts | Free online diagram software - Flowchart & process diagram, Network diagram, BPMN diagrams, Sitemap, Organisation chart, Wireframe, business drawing software",
   #"slug":"2c72bdd86db1",
   #"toread":"0",
   #"cached":null,
   #"code":null,
   #"private":"0",
   #"user_id":"60410",
   #"snapshot_id":null,
   #"updated":"2011-02-14 17:52:29",
   #"in_collection":null,
   #"sertags":",application,graph,graphics,chart,design,diagram,diagramming,flowchart,tool,visualization,",
   #"source":"7",
   #"tags":[  
      #"application",
      #"graph",
      #"graphics",
      #"chart",
      #"design",
      #"diagram",
      #"diagramming",
      #"flowchart",
      #"tool",
      #"visualization"
   #],
   #"author_id":"60410",
   #"url_slug":"c9f75b6d4b90340713effa1ddac4f876778c4f1b",
   #"url_count":"145"
#};
