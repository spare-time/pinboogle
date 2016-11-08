# pinboogle
Full text search for pinboard.in pins

## Requirements

You should have docker and docker-compose installed. We built using python 3, but things may work on previous versions.

## Executing spider

To install scrapy python project dependencies:

    $ pip install -r requirements.txt
    $ scrapy crawl --logfile=data/spider.log --loglevel=INFO -o data/data.json -t json -a user=[PINBOARD_USERNAME] -a after=[NUMBER] pinboard
   
Where PINBOARD_USERNAME is the user name you are registered and NUMBER is from which timestamp you want to fetch pinboard links (use 1 to start from oldest).

## Solr

After scraping data and adding it to data folder, start solr container with:

    $ docker-compose up -d

Solr will start and precreate a core named 'pinboard' as default. 
Also `./data` folder will be available inside the container at `/var/data` folder. 
If you want to explore the container, login with:

    $ docker exec -ti pinboogle_solr_1 /bin/bash

You can also access the admin site at `http://{DOCKER_HOST}:8983/solr`

### Importing data

With Solr container running, use the following command to create all the 
fields needed for Pinboard json we got from scraping task:

    $ docker exec -ti pinboogle_solr_1 /var/data/schema_migration.sh

And the next command to import the json file:

    $ docker exec -it --user=solr pinboogle_solr_1 bin/post -c pinboard /var/data/[JSON_FILE]

## Search Frontend

Search interface is implemented with Flask and it's located on `./web` folder.

When you run docker-compose up you will see that another container will be built. To access it, go to your browser at:

    http://{DOCKER_HOST}:5000

Everything that you change on `web` folder will be reflected on container, if you change or add any dependency, rebuild the container with:

    $ docker-compose down
    $ docker-compose up -d --build

Frontend can fail if solr schema is different between users, sorry about that, this will be improved.
