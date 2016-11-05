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


# Sample Solr config
  #<field name="_root_" type="string" docValues="false" indexed="true" stored="false"/>
  #<field name="_text_" type="text_general" multiValued="true" indexed="true" stored="false"/>
  #<field name="_version_" type="long" indexed="true" stored="false"/>
  #<field name="author" type="string" docValues="true" indexed="true" stored="true"/>
  #<field name="created_at" type="tdate" docValues="true" indexed="true" stored="true"/>
  #<field name="description" type="string" indexed="true" stored="true"/>
  #<field name="html_code" type="tlong" docValues="true" indexed="true" stored="true"/>
  #<field name="html_content" type="text_general" indexed="true" stored="false"/>
  #<field name="html_content_size" type="tlongs" docValues="true" indexed="true" stored="true"/>
  #<field name="html_fetch_date" type="strings"/>
  #<field name="id" type="string" multiValued="false" indexed="true" required="true" stored="true"/>
  #<field name="link_id" type="tlongs"/>
  #<field name="link_url" type="strings"/>
  #<field name="link_url_slug" type="strings"/>
  #<field name="private" type="tlongs"/>
  #<field name="saved_by_others" type="tlongs"/>
  #<field name="tags" type="strings"/>
  #<field name="title" type="strings"/>
  #<field name="to_read" type="tlongs"/>

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
