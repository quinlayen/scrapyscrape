# scrapyscrape

This was a project used to gather detailed information on specific products.  Quite a bit of learning went into this project as I first used Selenium in order to work with the scripting, 
but through gaining and a more thorough understanding of more advanced Scrapy techniques I was able to accomplish the task.  The output is a json of the scraped fields.

### No information scraped from this site is outside the bounts of the robots.txt

## How to use
1. Fork and clone repository
2. Create an environment and install dependencies with the included requirements.txt
3. From within omegawatches\omegawatches folder run `scrapy crawl omega`
4. To create an output json file run `scrapy crawl omega -o <output file name>`
