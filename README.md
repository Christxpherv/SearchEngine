# README for search engine project

## crawler.py

### Description
The `crawler.py` script is responsible for web scraping using Scrapy. It defines a spider (`SimpleSpider`) that crawls a website (`http://example.com`), extracts URLs and page titles, and stores them in a JSON file (`output.json`).

### Usage
Run the crawler using the command %  scrapy runspider crawler.py -o output.json

## index.py 

### Description
The `index.py` file is should be executed second and it responsible for indexing the data from the output.json file 

### Usage
Run the index file by using whatever keybinds you have set to run your files

## GUI.py 

### Description
The `GUI.py` file should be executed lastly and it is responsible for establishing the routes and enabling the graphical aspects of the code using html files that should be in a directory called "templates" 

### Usage
Run the GUI, and access the link you are provided in the output to be able to access it on your browser
