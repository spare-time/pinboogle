# pinboogle
Full text search for pinboard.in pins

## Settting things up

To install python project dependencies:
```sh
$ pip install -r requirements.txt
```
## Executing spider

    $ scrapy crawl --logfile=data/spider.log --loglevel=INFO -o data/data.json -t json -a user=[PINBOARD_USERNAME] -a after=[NUMBER] pinboard
   
Where PINBOARD_USERNAME is the user name you are registered and NUMBER is from which timestamp you want to fetch pinboard links (use 1 to start from oldest).

## Importing to Solr

With Solr installed and running, use the following commands:

    $ ./bin/solr create -c [NAME]
    $ ./bin/post -c [NAME] path/to/data.json

Solr can complain about html_content filed being immense. Go to Solr web interface and change the type of this field to text_general and reimport using the command above.

Test the index with Search web interface at: http://localhost:8983/solr/#/[NAME]/query

