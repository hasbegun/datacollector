# datacollector

# How to build the docker image.
docker build -t datacollector2 .
or ./docker-build2.sh

# How to run scrapy on docker
For a list of scrapy commands,
>> docker run -v $(pwd):/workspace/app datacollector2

# To start a new project
>> docker run -v $(pwd):/workspace/app datacollector2 startproject example

# To crawl spiders
>> docker run -v $(pwd):/workspace/app datacollector2 crawl SPIDER_NAME
