# pinboogle
Full text search for pinboard.in pins

## Settting things up

To install python project dependencies:
```sh
$ pip install -r requirements.txt
```
## Executing spider

    scrapy crawl --logfile=data/spider.log --loglevel=INFO -o data/data.json -t jsonlines -a user=[PINBOARD_USERNAME] -a after=[NUMBER] pinboard
   
Where PINBOARD_USERNAME is the user name you are registered and NUMBER is from which timestamp you want to fetch pinboard links (use 1 to start from oldest).

The jsonlines format is better to process since a lot of links are expected.
