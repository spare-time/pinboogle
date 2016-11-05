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

## Solr

After scraping data and adding it to data folder, start solr container with:

    $ docker-compose up -d

Solr will start and precreate a core named 'pinboard' as default. Also the data folder will be available inside the container at /var/data folder. If you want to explore the container, login with:

    $ docker exec -t -i pinboogle_solr_1 /bin/bash

You can also access the admin site at http://localhost:8983/solr

### Importing data

With Solr container running, use the following commands:

    $ docker exec -it --user=solr pinboogle_solr_1 bin/post -c pinboard /var/data/[JSON_FILE]

Solr can complain about html_content filed being immense. Go to Solr web interface and change the type of this field to text_general and reimport using the command above. Or check items.py file to see a sample solr schema for this data model.

Search your links at http://localhost:8983/solr/#/pinboard/query

